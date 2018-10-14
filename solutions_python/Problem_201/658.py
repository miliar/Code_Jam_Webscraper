T = int(raw_input())
for i in range(T):
    N, K = map(int,raw_input().split())
    diff = N-K
    l = 0
    while K>>l:
        l+=1
    ll = 1<<l
    n = diff/ll
    r = diff%ll
    print 'Case #'+str(i+1)+':'+' '+str(n+ (1 if r >=ll/2 else 0))+' '+str(n)