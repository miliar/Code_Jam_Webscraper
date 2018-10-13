T = int(raw_input())

def add_farm(C,F,X):
    t = 0
    f = 0
    while True:
        if C/float(2+f*F) + X/float(2+(f+1)*F) > X/float(2+f*F):
            return(t + X/float(2+f*F))
        t += C/(2+f*F)
        f += 1

for x in range(T):
    line = raw_input()
    C, F, X = [float(a) for a in line.split()]
    t = add_farm(C,F,X)
    print("Case #{0}: {1}".format(x+1, t))


