<img src="https://raw.githubusercontent.com/PaulBernert/DBNA/master/images/dbnaHeading.PNG"/>

# University of Arizona - Coding Bootcamp - Final Project

## Research Objectives
This project aims to take the [raw data](https://github.com/PaulBernert/DBNA/blob/master/_data/2020-report/data_with_msas.csv) provided from the Doing Business North America report, calculate a rank and score to determine the _'Ease of Doing Business'_ (see the [Methodology](https://github.com/PaulBernert/DBNA/wiki/Ease-of-Doing-Business-Methodology) for explanation of what Ease of Doing Business measures). The effectiveness of the ranking/scoring process will be tested in an applied setting--using the calculated _'Ease of Doing Business'_ ranks to see if it correlates with business activity relative to the local population. 

Another primary goal of the project is to use Machine Learning algorithms (through Scikit-learn) to test multiple clustering algorithms to see which locations are the most similar in nature. The two clustering algorithms to be tested are KMeans and Affinity Propagation. After comparing these two clustering structures, the next step is to test the relationship between clusters and the _'Ease of Doing Business'_ ranks to see if there clusters are formed around ranks (whether ranks are a good representative of how locations are clustered).

These tests were chosen not only to test the effectiveness of the data-set in an analytical environment, but to also see whether regulatory burdens truly have an impact on business starts.

## About the Project

The Doing Business North America (DBNA) project annually provides objective measures of the scale and scope of business regulations in 130 cities across 92 states, provinces, and federal districts of the United States, Canada, and Mexico. It uses these measures to score and rank cities in regard to how easy or difficult it is to set up, operate, and shut down a business. 

Over the years, researchers have begun to understand how robust measurement and ranking of regulations that either enhance business activity or constrain it can provide substantial insight into economic outcomes. Objective measurements of those regulations have been vital in this understanding. Unlike many studies that measure regulations at the state level, this annual study measures the impact at the city level and does so for over 100 municipal jurisdictions across North America.

The Doing Business North America team collected data on 63 different regulatory and economic indicators across six different categories. The data collected came entirely from official and publicly-available sources.

## About the Data
<img src="https://raw.githubusercontent.com/PaulBernert/DBNA/master/images/categories.PNG"/>

This project manually collects data on primary regulatory burdens businesses face throughout the entire life-cycle of a business, ranging from Starting a Business to eventually Resolving Insolvency if the business were to shut down / go bankrupt. The report contains data on 63 regulatory indicators within the following six categories:
1. Starting a Business
2. Employing Workers
3. Getting Electricity
4. Paying Taxes
5. Land and Space Use
6. Resolving Insolvency

These six categories are then combined to create a catch-all value known as the _'Ease of Doing Business'_. This is the value used in all analysis for this project.

#### Special Thanks to Arizona State University and the Center for the Study of Economic Liberty
<img src="https://raw.githubusercontent.com/PaulBernert/DBNA/master/images/brands.PNG"/>

## Contributing

#### Fix/Edit Content

If you see an error or a place where content should be updated or improved, let the [Project Director](https://isearch.asu.edu/profile/2653923) know and we will work to correct that as soon as possible.

#### Financial Contribution

If you wish to financially contribute to the [Center for the Study of Economic Liberty](https://csel.asu.edu/), please visit our [giving page](https://csel.asu.edu/about/giving). All contributions are greatly appreciated and work towards continuing projects such as this one.

## License

The data for this project (found in `_data`) is free to use and made publicly-available for research and scholarly use. Sourcing information will be included at a later time.
