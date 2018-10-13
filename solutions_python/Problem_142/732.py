def func2(st,un):
    nc = 0
    i = 0
    while nc != un:
        if st[i] != st[i+1]:
            nc += 1
        i += 1
    c = 1
    while i < len(st)-1 and st[i] == st[i+1]:
        c += 1
        i += 1
    return c
    
def func(st):
    i = 0
    u = st[0]
    while i < len(st)-1:
        if st[i] != st[i+1]:
            u += st[i+1]
        i += 1
    return u

t = input()
for i in range(t):
    n = input()
    c = 0
    ar = []
    st = raw_input()
    ar.append(st)
    u = func(st)
    flag = 0
    #print u
    for j in range(1,n):
        st = raw_input()
        ar.append(st)
        #print st
        un = func(st)
        #print un
        if un != u:
            print "Case #"+str(i+1)+": Fegla won"
            flag = 1
            break
    if flag == 0:
        for k in range(len(u)):
            s = 0
            for j in range(n):
                #print k,j
                s += func2(ar[j],k)
            #print s
            a = round(float(s)/float(n),0)
            #print a
            for j in range(n):
                c += abs(a-func2(ar[j],k))#ar[j].count(u[k]))
                #print j,c
        print "Case #"+str(i+1)+": "+str(int(c))
