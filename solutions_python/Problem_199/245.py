
def flip(s,n,p):
    for i in range(p,p+n):
        if s[i]=='-':
            s[i]='+'
        else:
            s[i]='-'
    return s

def isallplus(s):
    for i in s:
        if i=='-':
            return False
    return True
    
for t in range(input()):
    s,k=raw_input().split()
    k=int(k)
    s=list(s)
    if isallplus(s):
        print "Case #"+str(t+1)+": 0"
        continue
    l=len(s)
    ct=0
    for i in range(l-k+1):
        if s[i]=='-':
            flip(s,k,i)
            ct+=1
            #print s,i,k
    if isallplus(s):
        print "Case #"+str(t+1)+": "+str(ct)
    else:
        print "Case #"+str(t+1)+": IMPOSSIBLE"
        
        
