'''
Created on 2013/04/13

@author: hanaue51
'''

import os
os.chdir("../../../data/2013/qualification/")
filename = "B-large"
postfix_in = ".in"
postfix_out = ".out"

def mowable(lawn, grassheights):
    result = True
    
    while len(grassheights) > 1:
        cols_to_mow = set()
        min_height = grassheights[0]
        
        for row in xrange(len(lawn)):
            cols_will_mow = []
            for col in xrange(len(lawn[row])):
                if lawn[row][col] == min_height:
                    cols_will_mow.append(col)
            if 0 < len(cols_will_mow) and len(cols_will_mow) < len(lawn[row]):
                cols_to_mow = cols_to_mow.union(cols_will_mow)
        
        for col in cols_to_mow:
            for row in xrange(len(lawn)):
                if lawn[row][col] != min_height:
                    result = False
                    break
            if not result:
                break
        
        if result:
            for row in xrange(len(lawn)):
                for col in xrange(len(lawn[row])):
                    if lawn[row][col] == min_height:
                        lawn[row][col] = grassheights[1]
            grassheights = grassheights[1:]
        else:
            break
    
    return result

results = []
format = "Case #%d: %s\n"

# read inputs
infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

cases_count = int(lines[0].strip())
lineno = 1
for i in xrange(cases_count):
    elems = lines[lineno].strip().split()
    height = int(elems[0])
    width = int(elems[1])
    lawn = []
    grassheights = set()
    for j in xrange(1, height + 1):
        lawn_row = [int(lawn_col) for lawn_col in lines[lineno + j].strip().split()]
        lawn.append(lawn_row)
        grassheights = grassheights.union(lawn_row)
    if mowable(lawn, sorted(grassheights)):
        results.append(format % (i + 1, "YES"))
    else:
        results.append(format % (i + 1, "NO"))
    lineno += height + 1

# write results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
    outfile.write(result)
outfile.close()
