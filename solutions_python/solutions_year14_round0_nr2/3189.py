#!/usr/bin/python
from decimal import *

def readInput():
    inputfile = open("B-large.in","r");
    inputlist = inputfile.readlines()                   # make list of string
    inputlist = [word.strip() for word in inputlist]    # remove \n from the list of string
    inputlist = [x for x in inputlist if x]             # remove empty string from the list of string
    
        
    inputfile.close()
    return inputlist

def result(input_list):
    templist = input_list[1:]
    case_count = int(input_list[0])
    inputlist = []
    temp_result = []
    result = []
    for i in templist:
        inputlist = inputlist + [i.split()]
    
    for i in range(0,len(inputlist)):
        for j in range(0,len(inputlist[i])):
            inputlist[i][j] = float(inputlist[i][j])
    
    for i in inputlist:
        
        temp = calc(i)
        temp_result = temp_result + [temp]
    
    #print temp_result
    for i in range(0,len(temp_result)):
        temp_result[i] = round(temp_result[i],7)
    
    for i in range(0,case_count):
        temp = "Case #" + str(i+1) + ": " + "{:.7f}".format(temp_result[i]) + "\n"
        result = result + [temp]
    
    return result

def addfarm(calclist):
    
    farmtime = calclist[4] + (calclist[0]/calclist[3])
    realprod = calclist[3] + calclist[1]
    newtime = farmtime + (calclist[2]/realprod)
    
    templist = [calclist[0]] + [calclist[1]] + [calclist[2]] + [realprod] + [farmtime] + [newtime]
    
    return templist

def calc(floatlist):
    cost = floatlist[0]
    prod = floatlist[1]
    req = floatlist[2]
    realprod = 2.0
    farmtime = 0.0
    time = req/2
    
    newlist = floatlist + [realprod] + [farmtime] + [time]
    
    #print newlist
    
    if cost>req:
        return req/2
    if cost<req:
        while True:
            
            templist = addfarm(newlist)
            
            cost = templist[0]
            prod = templist[1]
            req = templist[2]
            realprod = templist[3]
            farmtime = templist[4]
            newtime = templist[5]
            if newtime < time:    
                newlist = [cost] + [prod] + [req] + [realprod] + [farmtime] + [newtime]
                time = newtime
            else:
                return time

def writeOutput(result_list):
    outputfile = open("B-large.out","w")
    #print outputfile
    #outputfile.write('Output\n\n')
    #outputfile = outputfile.write('\n')
    for i in result_list:
        outputfile.write(i)
    
    outputfile.close()

input_list = readInput()


#print input_list

case_count = int(input_list[0])

#print case_count
#print type(case_count) 

result_list = result(input_list)

#print result_list

writeOutput(result_list)


