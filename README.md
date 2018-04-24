# Freelance-Web-Scrape

The python script web scrapes job categories from the website Freelance.  The dataset only retrieves information on the skill, how many jobs pertaining to that skill, and the category that the skill belongs to.

Note: Concerning how many jobs there are, I don't know what factors contribute to the number of jobs.  

## Requirements

In order to use this script you must have the following programs:

* Python 3
* Beautiful Soup 4
* pandas

## Installation

To install the required libraries, do the following:

### With pip
```
pip install pandas
pip install beautifulsoup4
```

__Note__: You might need to add `sudo` if you don't have elevated privileges.  You might also need to specify `pip3` instead of `pip`.

### With conda

pandas is already installed with Anaconda.  For Beautiful Soup, do the following:
```
conda install beautifulsoup4
```

__Note__: You might need to add `sudo` if you don't have elevated privileges.

## Running the script

The following commands can be used to run the Python script:

```
cd ./Freelance-Web-Scrape
python main.py [csv filename]
```

where _csv filename_ is optional.