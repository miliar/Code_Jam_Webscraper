f = open('in', 'r')
fout = open('out', 'w')
t = int(f.readline())
for casenum in range(1, t + 1):
    print casenum

    d, n = f.readline().split()
    d = int(d)
    n = int(n)
    big = 0.0
    for i in range(n):
        k, s = f.readline().split()
        k = int(k)
        s = int(s)
        time = (1.0 * d-k)/s
        if time > big:
            big = time
    ans = d/big
    fout.write("Case #{}: {}\n".format(casenum, ans))