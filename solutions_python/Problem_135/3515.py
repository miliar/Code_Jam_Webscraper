# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 07:38:24 2014

@author: ali
"""
f = open('input.txt','r')
f.readline()

input = [line.strip() for line in f]

def find_row(lt, row):
    return lt[int(row)].split(' ')

outputFile=open('output.txt','w')

lineNumber=0
while True:
    lt=input[:10]
    first=set(find_row(lt,lt[0])) 
    second=set( find_row(lt[5:], lt[5]))
    match_count=len(first & second)
#    print first 
#    print second
#    print match_count
    if match_count == 1:
        lineNumber=lineNumber+1
        print >>outputFile, "Case #%d: %d" % (lineNumber, int(list(first & second)[0]))
    
    if match_count > 1:
        lineNumber=lineNumber+1
        print >>outputFile, "Case #%d: %s" % (lineNumber, "Bad magician!")
    if match_count==0:
        lineNumber=lineNumber+1
        print >>outputFile, "Case #%d: %s" % (lineNumber, "Volunteer cheated!")
    input=input[10:]
    
    if len(input)<=0: 
        break
    
f.close()