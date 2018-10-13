import sys

test = int(sys.stdin.readline())
for t in range(test):
    inps = sys.stdin.readline()
    inpsp = inps.split()
    
    A = int(inpsp[0])
    B = int(inpsp[1])

    x = A
    res = 0
    while x<=B:
        sx = str(x)
        lenx = len(sx)
        i = 1
        gen = []
        while i < len(sx):
            ns = sx[i:]+sx[0:i]
            ins = int(ns)
            if ins>x and ins<=B and ins not in gen:
                gen.append(ins)
                res = res + 1
            i = i + 1
        x = x + 1
    print "Case #"+str(t+1)+": "+str(res)
