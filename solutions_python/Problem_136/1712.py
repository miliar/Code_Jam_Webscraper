'''
Created on 11/04/2014

@author: Javier
'''

import sys

sys.setrecursionlimit(150000000)

fileN = "B-small-attempt1.in";

inpF = open(fileN, "r")

cases = {}
current = 0;
totalCases = -1

for line in inpF:
    line = line.strip()
    
    if totalCases == -1:
        totalCases = int(line)
        continue
    
    data = line.split(" ")
    
    if len(data) == 3:
        tmpO = {
                'c': float(data[0]),
                'f': float(data[1]),
                'x': float(data[2]),
        }
        
        cases[current] = tmpO
        current += 1


bt = 0
#process
def cookies(tC, time, cps, c, f, x):
    global bt
    if time > bt:
        return bt
    
    
    maxTime = (x - tC) / cps;
    wait = time + maxTime
    
    if wait < bt:
        bt = wait
    
    if wait > bt:
        return bt
    
    timeToBuyFarm = (c / cps)
    if time + timeToBuyFarm > bt:
        return bt
    return cookies(tC, time + timeToBuyFarm, cps + f, c, f, x)
    
    #option 1: no buy farm
    #option 2: buy farm
        

def cookiesStart(c, f, x):
    global bt
    bt = x / 2.0
    return cookies(0.0, 0.0, 2.0, c, f, x)


for i in cases:
    result = cookiesStart(cases[i]['c'], cases[i]['f'], cases[i]['x'])
    
    print "Case #" + str(i + 1) + ": " + str(result)