f = open("B-large.in")
o = open("out2.txt", "w")
T = int(f.readline())

for i in range(T):
    q = f.readline()[:-1].split()
    q = [int(a) for a in q]
    n = q[0]
    s = q[1]
    p = q[2]
    g = q[3:]

    win  = 0
    maybe = 0
    for k in g:
        if k > 3*p-3:
            win+=1
        elif k < 3*p-4 or k < p:
            pass
        else:
            maybe+=1
    o.write("Case #%d: %d\n"%(i+1, win+min(maybe,s)))
o.close()
