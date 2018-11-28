fin = open('B-large.in','r')

lines = fin.readlines()

T = int(lines.pop(0))
for i in range(T):
    line = lines.pop(0).split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])

    cookies = 0
    cps = 2.
    total_time = 0

    while True:
        t1 = X/cps

        t2 = C/cps + X/(F+cps)

        if t1 < t2:
            total_time += X/cps
            break
        else:
            total_time += C/cps
            cps += F

    print "Case #" + str(i+1) + ": " + str(total_time)


