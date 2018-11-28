for _ in xrange(input()):
    s,k=map(str,raw_input().split())
    k=int(k)
    a,c=[],0
    for i in xrange(len(s)):
        a.append(-1 if s[i]=='-' else 1)
    for i in xrange(len(s)-k+1):
        if a[i]==-1:
            a=a[:i]+map(lambda x:-x,a[i:i+k])+a[i+k:]
            c+=1
    if -1 in a[-1:-(k+1):-1]:
        print "Case #"+str(_+1)+": Impossible"
    else:
        print "Case #"+str(_+1)+": "+str(c)
