t = int(raw_input())
for m in range(t):
    d,h = raw_input().split()
    d,h = [int(d),int(h)]
    inp = []
    for i in range(h):
        k,s = raw_input().split()
        val = [int(k),int(s)]
        inp.append(val)
    sp = []
    x = 0
    for i in range(h):
        x = float(d-inp[i][0])/float(inp[i][1])
        x = float(d)/float(x)
        sp.append(x)
        
    print "Case #%d: %.6f"%(m+1,min(sp))   
        
