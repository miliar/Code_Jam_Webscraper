from math import *

fi=open("B-small-attempt5.in","r")
fo=open("B-small-attempt5.out","w")
n=int(fi.readline())

for caseNo in range(n):
        maxHeight=9
        minTime=maxHeight
        D=int(fi.readline())
        plates=fi.readline().strip().split()
        plates=map(int, plates)
        plates.sort()
        
        for h in range(1,maxHeight):
                t=h
                for plate in plates:
                        t=t+ceil(float(plate)/h)
                t=t-D
                if t<minTime:
                        minTime=t
        fo.write("Case #"+str(caseNo+1)+": "+str(int(minTime))+"\n")
fi.close()
fo.close()
