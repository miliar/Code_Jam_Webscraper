f=open('A-large.in','r')
r=open('out.out','w')
t=int(f.readline().strip('\n'))
for k in range(t):
    a=[]
    flag=0
    for i in range(4):
        t=f.readline().strip('\n')
        b=[j for j in t]
        a.append(b)
    if flag==0:
        for i in range(4):
            j=[a[i][0],a[i][1],a[i][2],a[i][3]]
            j.sort()
            j="".join(j)
            if j=='TXXX' or j=='XXXX':
                r.write("Case #"+str(k+1)+": X won")
                #print "Case #"+str(k+1)+": X won"
                flag=1
                break
            j=[a[0][i],a[1][i],a[2][i],a[3][i]]
            j.sort()
            j="".join(j)
            if j=='TXXX' or j=='XXXX':
                r.write("Case #"+str(k+1)+": X won")
                #print "Case #"+str(k+1)+": X won"
                flag=1
                break
        if flag==0:
            j=[a[0][0],a[1][1],a[2][2],a[3][3]]
            j.sort()
            j="".join(j)
            if j=='TXXX' or j=='XXXX':
                r.write("Case #"+str(k+1)+": X won")
                #print "Case #"+str(k+1)+": X won"
                flag=1
            j=[a[0][3],a[1][2],a[2][1],a[3][0]]
            j.sort()
            j="".join(j)
            if j=='TXXX' or j=='XXXX':
                r.write("Case #"+str(k+1)+": X won")
                #print "Case #"+str(k+1)+": X won"
                flag=1
    if flag==0:
        for i in range(4):
            j=[a[i][0],a[i][1],a[i][2],a[i][3]]
            j.sort()
            j="".join(j)
            if j=='OOOO' or j=='OOOT':
                r.write("Case #"+str(k+1)+": O won")
                #print "Case #"+str(k+1)+": O won"
                flag=1
                break
            j=[a[0][i],a[1][i],a[2][i],a[3][i]]
            j.sort()
            j="".join(j)
            if j=='OOOT' or j=='OOOO':
                r.write("Case #"+str(k+1)+": O won")
                #print "Case #"+str(k+1)+": O won"
                flag=1
                break
        if flag==0:
            j=[a[0][0],a[1][1],a[2][2],a[3][3]]
            j.sort()
            j="".join(j)
            if j=='OOOT' or j=='OOOO':
                r.write("Case #"+str(k+1)+": O won")
                #print "Case #"+str(k+1)+": O won"
                flag=1
            j=[a[0][3],a[1][2],a[2][1],a[3][0]]
            j.sort()
            j="".join(j)
            if j=='OOOT' or j=='OOOO':
                r.write("Case #"+str(k+1)+": O won")
                #print "Case #"+str(k+1)+": O won"
                flag=1
    if flag==0:
        for i in a:
            if '.' in i:
                r.write("Case #"+str(k+1)+": Game has not completed")
                #print "Case #"+str(k+1)+": Game has not completed"
                flag=1
                break
    if flag==0:
        r.write("Case #"+str(k+1)+": Draw")
        #print "Case #"+str(k+1)+": Draw"
    f.readline()
    r.write('\n')
r.close()
f.close()
