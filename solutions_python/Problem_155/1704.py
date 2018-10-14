import os
import sys

fname = 'A-large'
with open(fname+'.in') as f:
    lines = f.readlines()

T = int(lines[0].replace('\n',''))

t = 1

outfile = open(fname+'.out','w')

while t<=T:
    count = 0
    line = lines[t]
    lineitem = line.split(' ')
    smax = int(lineitem[0])
    s = list(lineitem[1])

    standingCount = 0

    for i in range(smax+1):
        if i>standingCount:
            count+=(i-standingCount)
            standingCount+=(i-standingCount)
        standingCount+=int(s[i])

    outfile.write("""Case #%s: %s\n""" %(t,count))
    t+=1

outfile.close()
