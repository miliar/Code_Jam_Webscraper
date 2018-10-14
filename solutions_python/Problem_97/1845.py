
f = open(r"C:\Users\User\Downloads\C-small-attempt0.in", "r")
#f = open("A-small-input.inp", "r")

T = int(f.readline().strip())

for t in range(T):
    A, B = map(int, f.readline().strip().split())

    res = set()

    while A < B:
        n = str(A)

        for i in range(1, len(n)):
            m = n[-i:] + n[:-i]

            if int (n) < int(m) and int(m) <= B:
                res.add((n,m))

        A += 1

    print "Case #%d: %d" % (t+1, len(res))   
