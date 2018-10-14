fl = open('B-large (2).in','r')
case=int(fl.readline())

for j in range(case):
    a=0
    
    z=fl.readline().split()
    dicinvoke={}
    for x in range(int(z[a])):
        a+=1
        l=list(z[a])
        dicinvoke[l[0]]={l[1]:l[2]}
        dicinvoke[l[1]]={l[0]:l[2]}
    oppose=[]
    a+=1
    for x in range(int(z[a])):
        a+=1
        l=list(z[a])
        oppose.append(l)
    a+=2
    st=list(z[a])
    l=[]
    for i in st:
        l.append(i)
        if len(l)>=2:
            try:
#                print dicinvoke[l[-1]][l[-2]]
                a=[]
                a.extend(l[:-2])
                a.append(dicinvoke[l[-1]][l[-2]])
                l=a
            except: pass
        try:
            for x in l[:-1]:
                for [k,d] in oppose:
                    if (k==x and d==l[-1])or(k==l[-1] and d==x):
                        l=[]
        except: pass
    print "Case #%d:"%(j+1),l
        

