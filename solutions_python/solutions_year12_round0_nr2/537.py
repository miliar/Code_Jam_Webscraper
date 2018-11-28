#!/usr/bin/python
import sys
import csv

def dancingGooglers(inpfile, outfile):
    fid = file(inpfile)
    numCases = fid.readline()
    numCases = int(numCases[:-1])

    fidOut = file(outfile, 'w')
  
    reader = csv.reader(fid, delimiter=' ')

    ca = 0
    for d in reader:
        ca = ca +1
        thres1 = max(int(d[2])*3-2,int(d[2]))
        thres2 = max(int(d[2])*3-4,int(d[2]))
        S = int(d[1])
        data = d[3:]
        counter = 0
        for di in data:
           if (int(di)>=thres1):
               counter = counter + 1
           elif (int(di)>=thres2 and S>0) :
               counter = counter + 1
               S = S-1
        fidOut.write('Case #%d: %d\n' % (ca, counter)) 
           
if __name__ == '__main__':
    dancingGooglers(sys.argv[1], sys.argv[2])



