fl = open('B-large.in','r')
case=int(fl.readline())
for j in range(case):
    z=fl.readline()
    z=z.strip()
    z=z.split()
    z=[int(x) for x in z]
    N=z[0]
    S=z[1]
    p=z[2]
    t=z[3:]
    l=[]
    lmin=[]
    lmax=[]
    for i in t:
        if i==0:
            l.append([0,[0,0,0]])
        elif i==1:
            l.append([0,[0,0,1]])
        elif i==29:
            l.append([0,[9,10,10]])
        elif i==30:
            l.append([0,[10,10,10]])
        else:
            if i%3==0:
                lmin.append([0,[i/3,i/3,i/3]])
                lmax.append([1,[i/3 -1,i/3,i/3 +1]])
            elif i%3==1:
                lmin.append([0,[i/3,i/3,i/3 +1]])
                lmax.append([1,[i/3 -1,i/3+1,i/3+1]])
            elif i%3==2:
                lmin.append([0,[i/3,i/3 +1,i/3 +1]])
                lmax.append([1,[i/3,i/3,i/3 +2]])
    for i in range(len(lmin)):
        if (p>=min(lmin[i][1]) and p<=max(lmin[i][1])) or min(lmin[i][1])>=p:
            l.append(lmin[i])
        elif max(lmax[i][1])<p and max(lmin[i][1])<p:
            l.append(lmin[i])
        else:
            if S != 0: 
                l.append(lmax[i])
                S=S-1
            else:
                l.append(lmin[i])
    result=0
    for i in l:
        if (p>=min(i[1]) and p<=max(i[1])) or min(i[1])>=p:
            result=result+1
    print "Case #%d:"%(j+1),result
        

