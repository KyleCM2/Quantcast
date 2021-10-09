#Kyle Choo Mang

#import for reading csv files and accessing cookies.csv
import os
import csv
import sys


#Checking if 4 arguments are giving
if (len(sys.argv) != 4):
    raise Exception("You have input more or less than 4 command line arguments.This program takes 4 CLAs only. ")

#variables for accessing the csv file
pythonScript = str(sys.argv[0])
csvF = str(sys.argv[1])
dateCon = str(sys.argv[2])
dateStr = str(sys.argv[3])

#Checking if file given is a .csv file
if(csvF[-4:] != ".csv"):
    raise Exception("You have given the wrong file type. This program takes CSV files only.")

#Checking if Date is proper format
if(dateCon != '-d'):
    raise Exception("You did not give the correct flag. -d flag must be the third argument.")

#Checking if Date is proper format
if(len(dateStr) != 10):
    raise Exception("You have given the wrong date format. Date format is YYYY-MM-DD.")

#Checkinf if file exists
if(os.path.isfile(csvF) == False):
    raise Exception("File does not exist.")

def maxCookie(csvFile,dateConfirm,dateString):
    filename = csvFile
    rows = []

    #dictionary for comparison
    dictID = {}
    
    #array for the output
    arrayCookie = []

    #opens the csv file in system's path and reads csv line by line
    with open(os.path.join(sys.path[0], filename), "r") as csvfile:
        csvreader = csv.reader(csvfile)  
        for row in csvreader:
            rows.append(row)

    #loops through the csv file and reads the date (up to the day)
    #checks if the cookie date matches the command line date
    #puts the cookie ID into a dictionary if cookie ID key does not exist
    #updates the cookie ID value if cookie ID key does exist
    for cookieRow in rows:
        if ((cookieRow[1].split("T")[0] == dateString)):
            dictID[cookieRow[0]]= 1 + dictID.get(cookieRow[0],0)

    #takes the max cookie value in the dictionary
    maxCookieCount = max(dictID.values())

    #loops through the dictionary to collect all cookie IDs that are equal to max cookie Count
    for cookie in dictID:
        if dictID[cookie] == maxCookieCount:
            arrayCookie.append(cookie)


    #prints the most active cookies
    for i in arrayCookie:
        print(i)


maxCookie(csvF,dateCon,dateStr)