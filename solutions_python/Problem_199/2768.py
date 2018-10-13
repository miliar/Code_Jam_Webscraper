t = input()

def ans(s,n):
    k = len(s)
    i = 0
    imp = False
    c = 0
    while i<k:
        #print s,i
        if(s[i]=='-'):
            if(i>=k-n+1):
                imp = True
                break
            j = i
            while(j<i+n and j<k):
                if(s[j]=='-'):
                    s[j] = '+'
                else:
                    
                    s[j] = '-'
                j+=1
            c+=1
        i+=1
    if imp:
        return 'IMPOSSIBLE'
    else:
        return str(c)
            
			


for i in xrange(t):
    s,n = raw_input().split()
    n = int(n)
    s = list(s)
    
    
    s = 'Case #%d: %s'%(i+1,ans(s,n))
    print s
    
