#!/usr/bin/python
import sys
    

n=len(sys.argv)
if(n<2):
   filename=raw_input("Enter the file name : ")
else:
    filename=sys.argv[1]

inFilename=filename+".in"
outFilename=filename+".out"
infile=open(inFilename)     
outfile = open(outFilename,"w")

C = int(infile.readline())
cases = 1
while(cases <= C):
    inStr  = infile.readline()
    inList = inStr.split()
    N = int(inList[0])
    M = int(inList[1])
    
    exists=['/']
    for i in range(0,N):
        inStr=infile.readline()
        exists.append(inStr[0:len(inStr)-1])

    tocreate=[]
    for i in range(0,M):
        inStr=infile.readline()
        tocreate.append(inStr[0:len(inStr)-1])
        
    exists.sort()
    tocreate.sort()
    #print "exists : ",exists
#    #print "to make",tocreate
    y=0

    for dir in tocreate:
        if not(dir in exists):
            num = 0
            dir=dir[1:]
            ldir=dir.split('/')
            str1=''
            #print "exists : ",exists
            #print "Starting the process ... for "+dir
            for d in ldir:
                #print d
                str1=str1+"/"+d
                if not(str1 in exists):
                    exists.append(str1)
                    exists.sort()
                    num=num+1
                    y=y+1
            #print "Number of dirs created ",num

            
    
    outStr = "Case #%d: %d \n" %(cases,y)
    outfile.write(outStr)
    cases = cases+1
    #print "End of one case ..."
    #print "****************************************************************"
    #print
