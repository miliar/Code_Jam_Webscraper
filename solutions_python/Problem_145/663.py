'''
Created on May 11, 2014

@author: matthias
'''
import sys

def read_nums(f):
    strs = f.readline().rstrip('\n').split('/')
    return [int(numeric_string) for numeric_string in strs]

f = open(sys.argv[1], 'r')
t = int(f.readline())
for i in range(1, t+1):
    [p, q] = read_nums(f)
    # check if q is exponent of 2
    exp2 = 1
    j = 0
    while (q > exp2) and (j < 15):
        exp2 *= 2
        j += 1
    if q != exp2:
        print "Case #" + str(i) + ": impossible"
        continue
    
    #find out lowest exponent of 2 
    perc = float(p) / float(q)
    exp2 = 1.0
    j = 0
    while (perc < exp2) and (j < 15):
        exp2 /= 2
        j += 1
        
    print "Case #" + str(i) + ": " + str(j)
