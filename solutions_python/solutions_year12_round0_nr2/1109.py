import sys
inp = open(sys.argv[1]);
outp = open(sys.argv[2], 'w');

count = int(inp.next())

i = 1

for line in inp:
    line = line.split()
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    s = 0
    m = 0
    scores = [int(x) for x in line[3:]]
    if p == 0:
        m = len(scores)
    else:
        for score in scores:
            if score < max(p * 3 - 4, 1):
                pass
            elif score < p * 3 - 2:
                s = s + 1
            else:
                m = m + 1
        m = m + min(s, S)
    outp.write("Case #%d: %d\n" % (i, m))
    i = i + 1
