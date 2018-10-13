def solve(smax, numbers):
#    print "solving {}".format(numbers)
    req = 0
    clapping = 0
    for i, count in enumerate(numbers):
#        print "req {} clapping {}".format(req, clapping)
#        print "processing {} {}".format(i, count)
        count = int(count)
        if count == 0: 
            continue
        if clapping >= i:
            clapping += count
        else:
            req += i - clapping
            clapping = i + count
#    print "final req {}".format(req)
    return req

fin = open("A-large.in.txt")
fout = open("out.large.txt", "w")

T = int(fin.readline())
for i in range(T):
    smax, numbers = fin.readline().strip().split()
    ans = solve(smax, numbers)
    fout.write("Case #{}: {}\n".format(i+1, ans))


