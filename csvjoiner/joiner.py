# Copyright (c) 2020 Ramon Quitales
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import csv
import os
from operator import itemgetter


class Joiner:
    def __init__(self, csv1: str, csv2: str, *argv: str):
        if os.stat(csv1).st_size > os.stat(csv2).st_size:
            csv2, csv1 = csv1, csv2

        self.csv_small_loc = csv1
        self.csv_large_loc = csv2
        self.join_key = [key for key in argv]

        self.merged = []
        self.small_csv = dict()

    def __find_join_idx(self, headers: list) -> list:
        join_locs = []
        for header in self.join_key:
            join_locs.append(headers.index(header))
        return join_locs

    def __inner_csv_small(self):
        with open(self.csv_small_loc) as csv_file:
            reader = csv.reader(csv_file)
            self.small_headers = next(reader)

            join_locs = self.__find_join_idx(self.small_headers)

            for row in reader:
                index_key = itemgetter(*join_locs)(row)
                if index_key not in self.small_csv:
                    self.small_csv[index_key] = [row]
                else:
                    self.small_csv[index_key].append(row)

    def __inner_csv_large(self, output: str, delimiter: str, quotechar: str):
        with open(self.csv_large_loc) as csv_file:
            reader = csv.reader(csv_file)

            self.large_headers = next(reader)
            join_locs = self.__find_join_idx(self.large_headers)

            self.headers = self.small_headers + \
                [header for idx, header in enumerate(
                    self.large_headers) if idx not in join_locs]

            if output != "":
                file = open(output, mode="w")
                csv_writer = csv.writer(
                    file, delimiter=delimiter, quotechar=quotechar)
                csv_writer.writerow(self.headers)

            for row in reader:
                merge_key = itemgetter(*join_locs)(row)
                if merge_key in self.small_csv:
                    for small_element in self.small_csv[merge_key]:
                        data = small_element + [element for idx,
                                                element in enumerate(row) if idx not in join_locs]

                        if output != "":
                            csv_writer.writerow(data)
                        else:
                            self.merged.append(data)

            if output != "":
                file.close()

    def __inner(self, output: str, delimiter: str, quotechar: str):
        self.merged = []
        self.__inner_csv_small()
        self.__inner_csv_large(output, delimiter, quotechar)

    def inner(self, output: str = "", delimiter: str = ",", quotechar: str = '"'):
        self.__inner(output, delimiter, quotechar)
        return {"headers": self.headers, "data": self.merged}
