#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saurabh
#
# Created:     14/04/2012
# Copyright:   (c) saurabh 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from collections import deque
from collections import defaultdict
def main():
    l=deque()
    m=deque()
    # getting  input
    fileName=input ('input file name')
    fileNameFirst=fileName.split('.')[0]
    fin=open(fileName)
    outFileName=fileNameFirst +'.out'
    fout=open(outFileName,'w')

    t=int(fin.readline())
    for testcase in range(1,t+1):
        d=defaultdict(list)
        count=0
        a,b=map(int,fin.readline().split(" "))
        for i in range(a,b):
            for j in range(a+1,b+1):
                if(i!=j):
                    l=deque(str(i))
                    m=deque(str(j))
                    if len(l)==len(m):
                        for length in range(1,len(l)):
                            l.rotate(1)
                            if((l==m) and ((j not in d[i])and(i not in d[j]))):
                                d[i].append(j)
                                count+=1
        #print("Case #%d: "%testcase+str(count))
        key='Case #'+str(testcase)+': '+str(count)+'\n'
        fout.write(key)
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
