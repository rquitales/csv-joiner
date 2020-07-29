<!--
 Copyright (c) 2020 Ramon Quitales
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/rquitales/csv-joiner-python">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">CSV Joiner</h3>

  <p align="center">
    Simple python package to merge CSV files
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project

This Python package enables merging of 2 CSV files. Currently, only inner joins are supported, with plans for more join operations.

This package will work fairly well on large datasets as it doesn't require reading both CSV files in memory. However, at least 1 CSV file must be small enough to be read in memory. The inner join is fairly efficient as it employs a HashMap to efficient find rows to be joined.

### Built With

- [Python 3.8](https://python.org)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps:

1. `pip3 install git+https://github.com/rquitales/csv-joiner-python.git`
2. Import `csvjoiner` within your Python script

### Prerequisites

This package requires Python 3.5 or greater in order to function properly. No other dependencies are required as it is implemented fully using base Python.

<!-- USAGE EXAMPLES -->
## Usage

- **Exporting merged data to CSV file:**

    ```{Python}
    import csvjoiner

    # Join on columns: colA, colB, colC
    join = csvjoiner.Joiner("/path/to/first/csv", "/path/to/second/csv", "colA", "colB", "colC")

    join.inner("/path/to/output/csv")
    ```

- **Converting merged data into Pandas dataframe:**
  
    ```{Python}
    import csvjoiner
    import pandas as pd

    # Join on columns: colA, colB, colC
    join = csvjoiner.Joiner("/path/to/first/csv", "/path/to/second/csv", "colA", "colB", "colC")

    merged_data = join.inner()
    df = pd.DataFrame(data=merged_data['data'], columns=merged_data['headers'])
    ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Ramon Quitales - oss@rquitales.com

Project Link: [https://github.com/rquitales/csv-joiner-python](https://github.com/rquitales/csv-joiner-python)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/rquitales/csv-joiner-python.svg?style=flat-square
[contributors-url]: https://github.com/rquitales/csv-joiner-python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rquitales/csv-joiner-python.svg?style=flat-square
[forks-url]: https://github.com/rquitales/csv-joiner-python/network/members
[stars-shield]: https://img.shields.io/github/stars/rquitales/csv-joiner-python.svg?style=flat-square
[stars-url]: https://github.com/rquitales/csv-joiner-python/stargazers
[issues-shield]: https://img.shields.io/github/issues/rquitales/csv-joiner-python.svg?style=flat-square
[issues-url]: https://github.com/rquitales/csv-joiner-python/issues
[license-shield]: https://img.shields.io/github/license/rquitales/csv-joiner-python.svg?style=flat-square
[license-url]: https://github.com/rquitales/csv-joiner-python/blob/master/LICENSE.txt