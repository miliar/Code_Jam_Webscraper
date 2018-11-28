def flip(s,j,k):
    l = ''
    for i in range(len(s)):
        if (i>=j and i<=j+k-1):
            if s[i] == '+':
                l += '-'
            else:
                l += '+'
        else:
            l += s[i]
    return l

a = raw_input()
inl = a.split("\n")
tc = int(inl[0])
del(inl[0])
cno = 0
for i in inl:
    cno += 1
    s,k = i.split()
    k = int(k)
    flag = 1
    count = 0
    for j in range(len(s)-k+1):
        if s[j] == '-':
            s = flip(s,j,k)
            count += 1
    for j in range(len(s)-k+1,len(s)):
        if s[j] == '-':
            flag = 0
    if flag == 0:
        print "Case #"+str(cno)+": IMPOSSIBLE"
    else:
        print "Case #"+str(cno)+": "+str(count)
