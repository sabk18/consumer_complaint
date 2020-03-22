#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:55:53 2020

@author: sabkhalid
"""


#import all required libraries:

import csv
import os 
import sys
import math
import collections

#################
#define path

#path = '/Users/sabkhalid/desktop/consumer_complaints'
#os.chdir(path)

#################

def sort_data(list_data):
    return sorted(list_data, key=lambda x: (x[1], x[0], x[2]))

def rounding_int(n):
    if n - math.floor(n) >= 0.5:
        return math.ceil(n)
    return math.floor(n)

def processing_file(data):
    
    
    
    data_column = []
    for columns in data[1:]:    
        date_received = columns[0]
        product = columns[1]
        company =columns[7]
        list_columns = [date_received, product, company]   
        data_column.append(list_columns)
        
    for list_2 in data_column:
        date = list_2[0]
        date_split= date.split("-")
        year=date_split[0]    
        list_2[0]= year
        
    Dic_output = {}
    for lst in sort_data(data_column):
        if '|'.join(lst[0:2]) in Dic_output:
            company = lst[2]
            Dic_output['|'.join(lst[0:2])].append(company)     
        else:        
            Dic_output['|'.join(lst[0:2])] = lst[2:]
            
    with open(output_file, mode="w") as csv_file:
        csvwriter = csv.writer(csv_file)   
                   
        for k, v in Dic_output.items():   
             
            keys= k.split('|')
            Year = keys[0]
            Product = keys[1].lower()
            
            complaints = len(v)
            
            unique_companies = len(set(x for x in v))
            
            counter = collections.Counter(v)
            complain_num = counter.values()
            highest_complaint = max(complain_num)
    
            complaints_percent = (highest_complaint/complaints)*100
            complaints_percent = rounding_int(complaints_percent)
            
    
#            if ',' in Product:
#                Product = '"' + Product + '"'
#            else:
#                Product
                
            csvwriter.writerow([Product, Year, complaints, unique_companies, complaints_percent])
                
    return csvwriter
   
    
if __name__ == "__main__":
    input_file=sys.argv[1]
    output_file=sys.argv[2]
    
    with open(input_file, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        data =list(reader) 
        processing_file(data)     
    
           
        



  
    
    
    