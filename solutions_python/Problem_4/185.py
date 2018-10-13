import math

def mycmp (x,y):
        if x>=0 and y>=0:
                return (-cmp(x,y))
        elif x<0 and y>=0:
                return 1
        elif x>=0 and y<0:
                return -1
        return (cmp(-x,-y))

def getmin (v1,v2,n):
        v1.sort(mycmp)
        v2.sort(mycmp)
        res=0
        for i in range (0,n):
             res += v1[i]*v2[n-1-i] 
	return res

fd = open ("A.in", "r")

n=int(fd.readline())
for i in range (1,n+1):
        n2=int(fd.readline())
        v1=map(int,fd.readline().strip('\n').split(" "))
        v2=map(int,fd.readline().strip('\n').split(" "))
        print "Case #" + str(i) + ": " + str(getmin (v1,v2,n2))
