def robot(units,ham):
    avg = (sum(ham)+units)/len(ham)
    nobs = []
    while max(ham) > avg:
        bop = []
        for i in ham:
            if i > avg:
                nobs.append(i)
            else:
                bop.append(i)
        ham = bop
        if len(ham) > 0:
            avg = (sum(ham)+units)/len(ham)
        else:
            avg = 0
            break
    x = 1
    for i in nobs:
        x = x * i
    x = x * (avg**len(ham))
    return x



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    units = float(raw_input())
    ham = [float(s) for s in raw_input().split(" ")]
    print "Case #{}: {}".format(i, robot(units,ham))