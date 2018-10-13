import math
import string
f=open('D:/codejam/C-small-attempt3.in')
bl=f.readlines()
f.close()
n=bl[0]
k=int(n)
i=1
pyes=0
f=open('D:/codejam/out.txt','w')
while i <= k :
    count=0
    m= bl[i].split()
    start=int(math.ceil(math.sqrt(int(m[0]))))
    stop=int(math.floor(math.sqrt(int(m[1]))))
    for t in range(start,stop+1) :
        if(str(t)[::-1] == str(t)) :
            if(str(t*t)[::-1]==str(t*t)) :
                count=count+1
    f.write('Case #'+ str(i) + ': '+(str(count) + '\n'))
    i=i+1
f.close()
