# Fetch North American Breeding bird data with mistnet train & test split

The code in this repository uses the scripts provided by [David
Harris](https://github.com/davharris) mistnet model to process the BBS data into
a training and test dataset, as well as cross validation folds. The mistnet
paper is available
[here](http://onlinelibrary.wiley.com/doi/10.1111/2041-210X.12332/full).

Please note: The dataset fetched here is proprietary. Please make sure to read
the terms of use [here](https://www.pwrc.usgs.gov/bbs/rawdata/).

The code downloads the BBS data, use David Harris's (modified) scripts to split
them into training and test sets, and saves the results as csvs into the
subfolder `csv_bird_data`.

Please note that the scripts have been updated to use the latest release of
the BBS dataset. This meant I had to remove some checks. I will run further
checks on the data in the coming months and make updates if required, but use at
your own risk for now!

## Requirements

To run, the code requires:

* python (tested under python 2.7.14)
* R (tested under 3.4.3) with packages `geosphere`, `raster`, `caret` and
  `lubridate`
* The UNIX command line tool `wget`

## How to run

Make sure (!) to clone this repository with its submodules by using:

`git clone --recurse-submodules CLONE_URL`

Once cloned, you should be able to simply run:

`python prepare_dataset.py`

If everything goes to plan, you should find a folder called `csv_bird_data` with
the following contents:

```
├── fold.ids.csv
├── in.test.csv
├── in.train.csv
├── latlon.csv
├── route.presence.absence.csv
├── species.data.csv
└── x.csv
```
