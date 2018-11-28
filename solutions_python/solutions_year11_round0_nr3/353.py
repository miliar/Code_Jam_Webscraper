# !\usr\bin\python

import sys

n=int(sys.stdin.readline())
old=n
while n>0:
    n=n-1
    x= int(sys.stdin.readline())
    lst=sys.stdin.readline().split()
    inlst=[]
    for i in lst:
        inlst.append(int(i))
    xres=0
    for i in inlst:
        xres=xres^i
    if xres == 0:
        inlst.sort()
        for j in range(len(inlst)-1):
            xpat=0
            xsean=0
            for i in range(j+1):
                xpat=xpat^inlst[i]
            for i in range(j+1,len(inlst)):
                xsean=xsean^inlst[i]
            if xpat==xsean:
                break
        xpat=0
        xsean=0
        for i in range(j+1):
            xpat=xpat+inlst[i]
        for i in range(j+1,len(inlst)):
            xsean=xsean+inlst[i]
        if xpat>=xsean:
            print "Case #" + str(old-n) + ": " + str(xpat)
        else:
            print "Case #" + str(old-n) + ": " + str(xsean)
    else:
        print "Case #" + str(old-n) + ": NO"
