import sys

def find_max(l, sean, pat):
    if len(l) > 0:
        p = [i for i in pat]
        p.append(l[0])
        s = [i for i in sean]
        s.append(l[0])
        m1 = find_max([i for i in l[1:]], [i for i in sean], p)
        m2 = find_max([i for i in l[1:]], s, [i for i in pat])
        return max(m1,m2)
    else:
        sean_sum = 0
        pat_sean = 0

        pat_sum = 0
        pat_pat = 0
        for i in sean:
            sean_sum += i
            pat_sean ^= i
        for i in pat:
            pat_sum += i
            pat_pat ^= i
        if sean_sum >= pat_sum and pat_pat == pat_sean and len(pat) > 0:
            return sean_sum
        return -1

if len(sys.argv) < 2:
    print "correct usage: python candies.py <filename>"
    sys.exit()

f = open(sys.argv[1], 'r')
line = f.readline()
count = 1
while line:
    line = f.readline()
    line = [int(i) for i in f.readline().split()]
    if len(line) < 1: continue
    m = find_max(line, [], [])
    if m > -1:
        print "Case #%d: %d" % (count, m)
    else:
        print "Case #%d: NO" % count
    count+=1

