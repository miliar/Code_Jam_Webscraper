f=open('C:/Users/chetan/Desktop/C-small-attempt0.in','r')
n=f.readline()
b=f.readlines()
f.close()
k=int(n)
i=0
py=0
while i <k :
    count=0
    m= b[i].split()
    start=int(m[0])
    end=int(m[1])
    p=start
    q=len(m[0])
    for p in range(start,end+1):
        for r in range (1,q):
            pair=str(p)[q-r:q]+str(p)[0:q-r]
            intp=int(pair)
            if intp > p and (intp <= end) and (intp != py) :
                count = count+1
                py=pair
    b[i]='Case #%s: %s\n' % (i+1,count)
    i=i+1
f=open('C:/Users/chetan/Desktop/outc.txt','w')
f.writelines(b)
f.close()
               


