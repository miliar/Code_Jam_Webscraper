for i in xrange(1,input()+1):
    print "Case #%d:"%(i),
    s=list(raw_input().strip())
    for j in xrange(len(s)-2,-1,-1):
        if s[j]>s[j+1]:
            s[j]=str(int(s[j])-1)
            for k in xrange(j+1,len(s)):
                s[k]='9'
    print int(''.join(s))
