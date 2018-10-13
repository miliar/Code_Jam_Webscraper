def int_num(wires):
    A = list(wires)
    B = list(wires)
    A.sort(lambda x,y: x[0]-y[0])
    B.sort(lambda x,y: y[1]-x[1])
    
    c = 0
    
    while len(A)>0:
        w1 = A.pop()
        for w2 in B:
            if w1 == w2:
                continue
            if w2[1]<w1[1]:
                break
            c = c+1
        B.remove(w1)
    return c
 
t = int(input())
       
for t_no in range(1,t+1):
    n = int(input())
    
    wires = list()
    for x in range(n):
        ab = raw_input().split()
        ab = map(int,ab)
        wires.append((ab[0],ab[1]))
        
    res = int_num(wires)
    print "Case #%d: %d" % (t_no, res)

