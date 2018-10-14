# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 02:11:30 2017

@author: boxerrebellion
"""

with open("B-small-attempt2.in") as inputfile:
    cases = inputfile.readlines()

tests = [ i[:-1] for i in cases]
results = []
for i in range(1, len(tests)):
    var = int(tests[i])    
    while True:
        if len(str(var)) == 1:
            results.append(var)            
            break
        check = True        
        for j in range(len(str(var))-1):
            if int(str(var)[j]) <= int(str(var)[j+1]):
                pass
            else:
                var -= 1
                check = False
                break
        if check:
            results.append(var)
            break

with open("result", "w") as outputfile:
    for i in range(len(results)):
        outputfile.write("Case #" + str(i+1) + ": " + str(results[i]) + "\n")
