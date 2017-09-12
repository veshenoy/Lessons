#this script will parse first column from the csv
#! /usr/bin/Python
import csv

variable = []
f=open("C:/Users/veshenoy/Desktop/input.txt","r")

for i in csv.reader(f, delimiter = ","):
    variable.append(long(i[0]))
    
print variable
variable.sort()
print "\n***************************************************\n"
print variable