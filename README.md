# Consumer_complaints

## Purpose
Identify the number of complaints for unique pairs of product and year and how these complaints are spread over companies. 

## Tasks
This Python script reads each row of the input file (complaints.csv) and does the following:
1. identifies unique pairs of product and year.
2. The total number of complaints for that product and year
3. Total number of companies receiving at least one complaint for that product and year
4. The highest percentage of total complaints filled against one company.

This information is extracted and written to a csv file (report.csv) that is exported to the output file. A run.sh is provided to execute the company_complaints.py file as well as provide a path for the input and output files. The run.sh script can be executed using 'bash run.sh' or './run.sh'

## STEPS

1. Modules imported:
*  sys
*  os
*  csv
*  collections
*  math

2. The first step was to open the csv file and read it into a list. Only columns that were needed were kept , the header was removed and then stored into a new list called data_column. The columns we choose were : Date received(0) , Product (1) and companies(7). 
3. Now comes processing the date column. The date was striped at '-' and only the year at index 0 was selected and applied to each list.
4. Now we have a list of list. each list has the date, product and company. I processed each list into a dictionary as key:value pairs. where key was 'date '|' product 'and the value was the company. This way we can now have unique pairs of product and year as the keys of the dictionary and companies as thier values. 
5. This dictionary is now used for the rest of the processing. we count the number of companies within the value assigned to each key (unique pair of product and year) and this is our total number of complaints for that unique product and year. Finding the unique companies inside the value, gives us the total number of companies receiving at least one complaint for that product and year(key). then Used counter from collections (faster than creating a dictioanry) to find the company with the maximum frequency within the value for each key, which is then divided by the total number of complaints and multiplied by 100 to get the percentage for the highest complaint. 
6. To have an output with the structure as requested in the challenge, The keys isnide the dictionary were split at '|' to get date and product which were stored under thier respective variables. Our final output writes the data (product, Year, number of complaints, unique companies (companies with at least one complaint), highest percenatge of complaint for a company) to a csv file 'export.csv'.

## Processing

To process the data as requested some fucntions were kept in mind:
1. Sorting the Product (alphabetically) and Year (ascending)
2. Change the product name to lower case.
3. Rounding the highest percentage to its whole number (if the decimal is between 0.5 and then round upwards to nearest whole number, if the decimal is less than 0.5 (not included) then round downwards)
4. If a product has comma between product names , then have the product in quotation marks in the output file.





