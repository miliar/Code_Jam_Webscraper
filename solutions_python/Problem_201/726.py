f = open('in', 'r')
fout = open('out', 'w')
t = int(f.readline())
for casenum in range(1, t + 1):
    print "printing casenum", casenum
    n, k = f.readline().split()
    if n == k:
        fout.write("Case #{}: {} {}\n".format(casenum, 0, 0))
        continue
    n = int(n)
    k = int(k)

    cur = 1

    tot = 0
    while tot + cur < k:
        n -= cur
        tot += cur
        cur *= 2
        # div = [n/cur] * cur
        # extra = n%cur
        # for i in range(extra):
        #     div[i] += 1

    n -= cur
    cur *= 2
    quotient = n/cur
    firstx_increment = n%cur
    if firstx_increment > cur/2:
        firstx_increment -= cur/2
        besar = quotient + 1
        if k - tot <= firstx_increment:
            kecil  = quotient + 1
        else:
            kecil = quotient
    else:
        kecil = quotient
        if k -tot <= firstx_increment:
            besar = quotient + 1
        else:
            besar = quotient

    # div = [n / cur] * cur
    # extra = n % cur
    # for i in range(extra):
    #     div[i] += 1
    # sz = len(div)/2
    # print tot, k, kecil, besar
    # for cur in zip(div[sz:], div[:sz]):
    #     print cur
    # ans = zip(div[sz:], div[:sz])[k - tot - 1]

    #
    # n -= cur
    # cur *= 2
    # div = [n / cur] * cur
    # extra = n % cur
    # for i in range(extra):
    #     div[i] += 1
    # print div
    #
    # n -= cur
    # cur *= 2
    # div = [n / cur] * cur
    # extra = n % cur
    # for i in range(extra):
    #     div[i] += 1
    # print div
    #
    # n -= cur
    # cur *= 2
    # div = [n / cur] * cur
    # extra = n % cur
    # for i in range(extra):
    #     div[i] += 1
    # print div
    #


    # kiri = toins - u - 1
    # kanan = v - toins - 1
    fout.write("Case #{}: {} {}\n".format(casenum, besar, kecil))
    #
