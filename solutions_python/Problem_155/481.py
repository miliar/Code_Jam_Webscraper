inputname = 'A-large.in'
outputname = 'output.out'
f = open(inputname)
fw = open(outputname, 'w')

T = int(f.readline().strip())

for t in range(T):
    d = f.readline().strip().split()
    n = int(d[0])
    l = d[1]
    total = 0
    summ = 0 + int(l[0])
    for i in range(1, n + 1):
        k = int(l[i])
        if summ < i and k > 0:
            total += (i - summ)
            summ = i
            # print total, summ
        summ += k
    fw.write('Case #%d: %d\n' % (t + 1, total))

f.close()
fw.close()
