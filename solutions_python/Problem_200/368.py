
def solve(n):

    s = map(int,list(str(n)))

    for i in xrange(len(s)-1,0,-1):
        if(s[i]<s[i-1]):
            for j in range(i,len(s)): s[j]=9
            s[i-1]=s[i-1]-1

    while(s[0]==0): s.remove(0)

    return ''.join(map(str,s))


t = int(raw_input())

for i in range(1,t+1):
    n = int(raw_input())
    print "Case #%d: %s" %(i,solve(n))
