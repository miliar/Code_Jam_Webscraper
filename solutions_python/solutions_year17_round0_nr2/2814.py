a = raw_input()
inl = a.split("\n")
tc = int(inl[0])
del(inl[0])
cno = 0
for z in range(tc):
    cno = cno+1
    l = len(inl[z])
    al = [i for i in range(l)]
    for i in range(l):
        al[i] = int(inl[z][i])  
    for i in range(len(al)-1):
        if al[i]>al[i+1]:
            k = i
            while (al[k]==al[i] and k>=0):
                k=k-1
            al[k+2:] = [9]*(l-k-2)
            al[k+1] -= 1
    ans = 0
    x = 1
    for i in range(len(al)-1,-1,-1): 
        ans += al[i]*x
        x *= 10
    print "Case #"+str(cno)+": "+str(ans)
