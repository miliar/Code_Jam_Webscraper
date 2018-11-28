#Filename: C.py
import math

def ispal(a):
    b = str(a)
    flag = True
    for i in range(len(b)/2):
        if b[i]!=b[len(b)-i-1]:
            flag = False
            break
    return flag



fin=file('C-small-attempt0.in')
fout=file('output.txt','w')
numcase = fin.readline()
curnum=0;
rows=fin.readlines()
#print rows

for line in rows:
    curnum+=1
    count=0
    palarr=[]
    left,right=line.split()
    for num in range(int(left),int(right)+1):
        if ispal(num):
            palarr.append(num)
    for i in range(0,len(palarr)):
        sqr=int(math.sqrt(palarr[i]))
        if sqr*sqr==palarr[i]:
            if ispal(sqr):
                count+=1
    fout.write('Case #%d: %d\n' %(curnum,count))

fin.close()
fout.close()
