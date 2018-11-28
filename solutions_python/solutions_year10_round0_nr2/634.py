from math import *

def max_div(a,b):
    if a<b :
        c=b
        b=a
        a=c
    while True:
        if a%b==0:
            return b
        else:
            d=a%b
            a=b
            b=d

            
            
#print max_div(11, 10)
f = open('B-small-attempt1.in', 'r')
fout = open('Download B-small.out', 'w')
T=int(f.readline())
for i in xrange(0, T):
    string = f.readline()
    N = int(string[0])
    list = str.split(string, ' ', N)
    for e in xrange(0, len(list)):
        list[e]=long(list[e])
    #print list
    div = 0
    if N==2:
        div=abs(list[1]-list[2])
    else:
        div=abs(list[1]-list[2])
        t=1
        while div==0:
            t=t+1
            div = abs(list[t]-list[t+1])
        for j in xrange(2, N):
            y=abs(list[j]-list[j+1])
            if (y!=0):
                    div = max_div(div,y)
    
    #print 'div='+str(div)
    #print list[1]
    k=max(list)%div
    if k==0:
        print 0
        value = 'Case #'+ str(i+1)+ ': 0\n'
    else:
        print div-k
        value = 'Case #'+ str(i+1)+ ': '+ str(div-k)+'\n'
    fout.write(value)
f.close()
fout.close()
