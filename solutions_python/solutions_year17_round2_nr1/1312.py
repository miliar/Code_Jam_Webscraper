t = int(raw_input().strip())

for i in range(t):
    d,n = map(int,raw_input().split())
  
    lis = []
    for j in range(n):
        k,s = map(int,raw_input().split())
        v = float(d - k)/float(s)
        v = float(d)/float(v)
        lis.append(v)
        
    ans = min(lis)

    print "Case #%d: %.6f"%(i+1,ans)
