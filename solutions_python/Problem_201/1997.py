inp = open("stalls.in", 'r')
opt = open("stalls.out", 'w')

T = None
Ns = []
Ks = []
for line in inp:
    if T is None:
        T = int(line)
    else:
        l = line.split(" ")
        Ns.append(int(l[0]))
        Ks.append(int(l[1]))

# plan: person always wants to find the largest empty interval, then chose midpoint (if it's even, round down)
# keep track of a list of empty interval sizes
# when a person arrives, find largest empty interval and replace it with 2 new intervals

r = None
l = None
for x in range(len(Ns)):
    intervals = [Ns[x]]
    ppl = 0
    while ppl != Ks[x]:
        m = max(intervals)
        mi = intervals.index(m)
        l = int(m/2)
        r = l
        if m % 2 == 0:
            l -= 1
        if r != 0:
            intervals.insert(mi+1, r)
        if l != 0:
            intervals.insert(mi+1, l)
        intervals.pop(mi)
        ppl += 1
    opt.write("Case #" + str(x+1) + ": " + str(r) + " " + str(l) + "\n")

opt.close()
