T = int(input())
for t in range(1,T+1):
    n, k = map(int,input().split())
    m = 1
    s = {n:1}
    nmax = n
    nmin = n
    while k > m:
        k -= m
        m *= 2
        s1 = {}
        for p in s:
            nr = p//2
            nl = p - 1 - nr
            if nr in s1:
                s1[nr] += s[p]
            else:
                s1[nr] = s[p]
            if nl in s1:
                s1[nl] += s[p]
            else:
                s1[nl] = s[p]                
            
        s = s1  
    ls = sorted(s,reverse=True)
    for p in ls:
  #      print(k,s[p])
        k -= s[p]
        if k <= 0:
            rmax = p//2
            rmin = p - 1 - rmax
            break
    print('Case #'+str(t)+':', rmax, rmin)
        
        
        
        
        
        