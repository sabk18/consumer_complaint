#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:55:53 2020

@author: sabkhalid
"""


#import all required libraries:
#######################
import csv
import sys
import math
import collections
import unittest 

########################

class TestCC(unittest.TestCase):
    
    def test_rounding_up(self):
        self.assertEqual(rounding_percent(15.5), 16)
        self.assertEqual(rounding_percent(15.7), 16 )
        
    def test_rounding_down(self):
        self.assertNotEqual(rounding_percent(15.4), 16)
             
########################

def sort_data(list_data):
    return sorted(list_data, key=lambda x: (x[1], x[0], x[2]))

def rounding_percent(n):
    if n - math.floor(n) >= 0.5:
        return math.ceil(n)
    return math.floor(n)

def column_slicing(input_data):
    data_columns = []
    for columns in input_data[1:]:    
        date_received = columns[0]
        product = columns[1]
        company =columns[7]
        list_columns = [date_received, product, company]   
        data_columns.append(list_columns)
    return data_columns
            
def processing_data(data):
    
    data = column_slicing(data)    #date formatting 
    for lst in data:
        date = lst[0]
        if date != '':
            date_split= date.split("-")
            year=date_split[0]    
            lst[0]= year
        else:
            lst[0] ='NaN'
        
    Dic_output = {}
    for lst in sort_data(data):
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
            complaints_percent = rounding_percent(complaints_percent)
                
            csvwriter.writerow([Product, Year, complaints, unique_companies, complaints_percent])
                
    return csvwriter
       
if __name__ == "__main__":
    input_file=sys.argv[1]
    output_file=sys.argv[2]
    
    with open(input_file, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        data =list(reader) 
        processing_data(data)  
   
        
    
           
        



  
    
    
    