t=int(raw_input())
for cas in xrange(1,t+1):
    n=int(raw_input())
    while '0' in str(n):
        for i in xrange(0, len(str(n))):
            if str(n)[i]=='0':
                a=int(''.join(str(n)[i:]))
                n=n-a-1;
                break
    while str(n) !=''.join(sorted(str(n))):
        n-=1
    print "Case #{}: {}".format(cas,n)
