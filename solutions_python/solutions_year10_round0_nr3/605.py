file = open("C-small-attempt0.in","r")

t = int(file.readline())

for i in range(t):
    rkn = file.readline().split(" ")
    r = int(rkn[0])
    k = int(rkn[1])
    n = int(rkn[2])
    
    q = file.readline().split()
    for b in range(n):
        q[b] = int(q[b])
    
    gsum = sum(q)
    
    s = 0
    for b in range(r):
        p = 0
        while 1:
            f = q[0]
            wp = p+f
            if wp <= k and wp <= gsum:
                p=p+f
                q.append(q.pop(0))
            else:
                s+=p
                break
    print "Case #%d:" %(i+1),s 