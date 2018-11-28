inPath = 'A-small-attempt0.in'
outPath = "A-small-attempt0.out"
with open(outPath,'w') as outf:
    with open(inPath) as inf:
        n = int(inf.readline().strip())
        for case in xrange(1, n+1):
            row1 = int(inf.readline().strip())
            m1 = []
            for r in xrange(4):
                m1.append(inf.readline().strip().split())
            row1s = set(m1[row1 - 1])
            row2 = int(inf.readline().strip())
            m2 = []
            for r in xrange(4):
                m2.append(inf.readline().strip().split())
            row2s = set(m2[row2 - 1])
            result = row1s.intersection(row2s)
            if len(result) == 0:
                outf.write("Case #" + str(case) + ": " + "Volunteer cheated!" + '\n')
            elif len(result) == 1:
                num = result.pop()
                outf.write("Case #" + str(case) + ": " + num + '\n')
            else:
                outf.write("Case #" + str(case) + ": " + "Bad magician!" + '\n')
            
