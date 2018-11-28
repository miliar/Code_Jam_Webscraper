import re
from Numeric import *

N = int(raw_input())

wc = 'welcome to code jam '
wcl = len(wc)

for x in xrange(0,N):
    line = raw_input()
    line += ' '
    l = len(line)
    arr = zeros((l,wcl))    

    for i in xrange(0,l):
        for j in xrange(0,wcl):

            if line[i] == wc[j]: 
                if j > 0:
                    t = 0
                    for k in xrange(0,i):
                        if line[k] == wc[j-1]:
                            t+=arr[k][j-1]%10000
                    arr[i][j] = t%10000
                else:
                    arr[i][j] = 1                    
            else:
                arr[i][j] = arr[i-1][j]%10000
   
#    for i in xrange(0,l):
#        print line[i],arr[i]

    print "Case #"+str(x+1)+": "+str(arr[l-1][wcl-1]).rjust(4,'0')
            
