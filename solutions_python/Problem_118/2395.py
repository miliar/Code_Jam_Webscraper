'''
Created on Apr 13, 2013

@author: vimuthfernando
'''
import math

def isPalin(num):
    nstr = str(num)
    return True if nstr==nstr[::-1] else False



f = open("C-small-attempt0.in",'r')
fout = open("output.txt",'w')
cases = int(f.readline())

for i in xrange(cases):
    count = 0
    lower,upper = [int(j) for j in f.readline().split(' ')]
    upper = math.floor((math.sqrt(upper)))
    x = int(math.ceil(math.sqrt(lower)))
    while (x<=upper):
        if isPalin(x):
            if isPalin(x**2):
                count += 1
        x+=1
    
    fout.write("Case #%d: %d\n" % (int(int(i)+1),count))
    
fout.close()