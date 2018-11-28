inputname = 'B-large.in'
outputname = 'output2.out'
f = open(inputname)
fw = open(outputname, 'w')

T = int(f.readline().strip())

for t in range(T):
    D = int(f.readline().strip())
    maxP = 0
    l = []

    for pi in f.readline().strip().split():
        temp = int(pi)
        if maxP < temp:
            maxP = temp
        l.append(temp)

    mintotal = maxP
    # print maxP
    if maxP > 2:
        for i in range(2, maxP + 1):
            total = i
            for pi in l:
                total += max(0, ((pi - 1) / i))

            if total < mintotal:
                mintotal = total

    fw.write('Case #%d: %d\n' % (t + 1, mintotal))

f.close()
fw.close()
