
import fileinput

f = fileinput.input()

ncase = int(f.readline())

for i in range(ncase):
    l = f.readline().split()
    seq = l[1]

    cum = 0
    add = 0

    for k, ns in enumerate(seq):
        n = int(ns)
        if k > cum:
            add += (k-cum)
            cum = k + n
        else:
            cum += n

    print("Case #%d: %d" % (i+1, add))


