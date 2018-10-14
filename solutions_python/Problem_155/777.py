t = input()
count = 0
for i in xrange(t):
    n,s = raw_input().strip().split()
    n = int(n)
    z = len(s)
    x = int(s[0])
    y = 0
    for j in xrange(1,n+1):
        if x>=j:
            x=x+int(s[j])
        else:
            y = y+(j-x)
            x = x+(j-x)+int(s[j])
    ans = "Case #%d: %d"%(count+1,y)
    print ans
        
    count+=1
