import sys
di=dict()

f1=open(sys.argv[1])
f1=f1.readlines()
f2=open(sys.argv[2])
f2=f2.readlines()

all=[chr(i) for i in range(97,123)]

aa=set()
bb=set()

for i in range(0,len(f1)):
    a=f1[i]
    b=f2[i][9:]
    for k in range(0,len(a)):
        if a[k] in all:
            aa.add(a[k])
            bb.add(b[k])
            di[a[k]]=b[k]

for i in all:
    if not i in aa:
        a=i
    if not i in bb:
        b=i
di[a]=b
            
#print di,len(di)

f3=open(sys.argv[3])
f3=f3.readlines()[1:]
i=0
for now in f3:
    i+=1
    print "Case #"+str(i)+":",
    ans=""
    for j in now:
        if j in di:
            ans+=di[j]
        else:
            if j!='\n':
                ans+=j
    print ans




    
