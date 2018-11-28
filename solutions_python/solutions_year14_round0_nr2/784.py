def do(c,f,x): 
    start = 0.0
    k = 2.0
    while (k+f) * c / f <= x:
        #print c/k, (k+f)*c/f 
        start += c / k
        k += f
    return start + x / k

#print do(500.0, 4.0, 2000.0)

t = int(raw_input())
for i in xrange(t):
    c,f,x = map(float,raw_input().split())
    print "Case #{}: {}".format(i+1,do(c,f,x))
