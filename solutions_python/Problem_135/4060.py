#!/bin/sh

#  MagicTrick.py
#  
#
#  Created by alifya on 2014-04-12.
#
"""ASSUMPTIONS
# This program assumes that:
    - The user has a version of python 2.7 installed in hes/her operating system
   """
import argparse
import sys
import csv
import collections
# Getrow takes in the row the volunteered has provided and a representation of the list and returns a list of the row the number is in.
def getrow(num,list):
    if num == 1:
        row = list[0:4]
    elif num == 2:
        row = list[4:8]
    elif num == 3:
        row = list[8:12]
    elif num == 4:
        row = list[12:16]

    return row
# This is what the user will use to read the input provided.
def csvread():
    with open(sys.argv[1], 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        newlist = []
        for row in spamreader:
            for i in row:
                newlist.append(int(i))
    
    return newlist

# This is what makes the magician perform hes magic. By comparing both rows if the card arrangements are different, the magician returns the number that appears to be duplicated in both rows returned from getrows.
def magic(r1,r2):
    num = []
    for i in r1:
        if i in r2:
            num.append(i)
    return num

def checkrows(r1, r2):
    check = False
    for i in r1:
        if i in r2:
            check = True
    return check

     
def main():

 
    
    #next = cmd_parse()
    input = csvread()

    a = 1 # I initialized this variable to keep track of where we are in our system arguments.
    # we want to iterate over T amount of Test cases therefor because input[0] provides the number of test cases we will iterate over the range.
    for i in range(input[0]):
        # the first row the volunteer provides
        firstselection = input[a]
        
        #we increment the argument by 1 as we are moving to the next part of the argument
        a += 1
        # We will make a list out of the first arrangement provided as it will help better represent the problem. We then increment a by 16 as each arrangement consists of 16 cards (16inputs in python)
        firstarrangement = input[a:(a+16)]
        
        a = a + 16
        # the second selection is similar to the way we made the first selections
        secondselection = input[a]
        
        a = a + 1
        secondarrangement = input[a:(a+16)]
        
        a = a + 16
        Row1 = getrow(firstselection,firstarrangement)
        
        Row2 = getrow(secondselection,secondarrangement)
        num = magic(Row1,Row2)
        
        #This case tests to see whether the magician is a bad magician.
        if (cmp(firstarrangement,secondarrangement) == 0) and (firstselection == secondselection):
            print 'Case #%d: Bad magician!' %(i+1)
        # This is to see whether the volunteer cheated
        elif (cmp(firstarrangement,secondarrangement) == 0) and not (firstselection == secondselection):
            print 'Case #%d: Volunteer cheated!' %(i+1)
        #Otherwise we get the rows provided by the user and compare them to see if they have a matching number and return that matching number
    
        elif checkrows(Row1, Row2) == True and len(num) == 1:
            
            print 'Case #%d: %d' %(i+1,num[0])
        elif checkrows(Row1, Row2) == True and len(num) > 1:
            print 'Case #%d: Bad magician!' %(i+1)
        else:
            print 'Case #%d: Volunteer cheated!' %(i+1)

    print checkrows([1,4,5,6],[4,7,8,9])

if __name__ == '__main__':
    main()