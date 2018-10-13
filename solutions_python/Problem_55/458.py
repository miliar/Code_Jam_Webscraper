def p(str):
		#print str
		pass


def readline():
    import sys
    f = open(sys.argv[1])
    T = int(f.readline()[:-1])
    p(T)
    for t in range(T):
        l = f.readline()[:-1].split()
        R = int(l[0])
        k = int(l[1])
        N = int(l[2])
        p(l)
        
        m = f.readline()[:-1].split()
        m = map(lambda x: int(x), m)
        p(m)
        s = solve(R,k,m)
        print("Case #%d: %d" %( t+1, s ))


def solve(R, k, m):
    cost = 0
    for r in range(R):
        sum = 0
        n = []
        while 1:
            if len(m) == 0 or sum + m[0] > k:
                p("go!")
                cost += sum
                m += n
                break
            else:
                a = m.pop(0)
                p("%d set:" % a)
                n.append(a)
                sum += a

    p(cost)
    return cost
readline()
