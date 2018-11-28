import math
import string
f=open("C-small-attempt0.in")
out=open("output.txt",'w')
def inp():
    for i in f:
        return i

def isFairSquare(i,j):
    if str(j)==str(j)[::-1] and str(i)==str(i)[::-1]:
        #print j
        return True
    return False
t=int(inp())
for i in range(t):
    count=0
    start,end=[int(j) for j in inp().split()]
    for j in range(start,end+1):
        if math.ceil(math.sqrt(j))==math.sqrt(j):
            if isFairSquare(int(math.sqrt(j)),j):
                count+=1
    #print count 
    out.write("Case #"+str(i+1)+(": ")+str(count)+"\n")
f.close()
out.close()
