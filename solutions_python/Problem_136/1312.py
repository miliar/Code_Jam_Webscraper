fin = open("B.in", "r")

T = int(fin.readline())

for i in range(T):
    C, F, X = [float(a) for a in fin.readline().split()]

    rate = 2.0
    time = oldtime = 0.0
    expect = oldexpect = X / rate

    while (time + expect <= oldtime + oldexpect):
        oldtime = time
        oldexpect = expect
        time += C / rate
        rate += F
        expect = X / rate

    print "Case #" + str(i + 1) + ": " + str(oldtime + oldexpect)
