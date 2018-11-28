t = int(input())

for i in range(t):
    d,n = map(int,raw_input().strip().split())

    ls = list()
    for j in range(n):
        k,s = map(int,raw_input().strip().split())
        t = float(float(d-k)/float(s))
        ls.append(t)
    spd = float(float(d)/float(max(ls)))
    
    print "Case #%d:"%(i+1),spd
