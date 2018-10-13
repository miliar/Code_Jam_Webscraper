fileName = "B-small-attempt2"
fin = open(fileName + ".in", "r")
fout = open(fileName + ".out", "w")

T = int(fin.readline())
print T

for caseID in xrange(1, T+1):
    nonbase = dict()
    combine = dict()
    oppose = dict()
    temp = fin.readline().split()
    print temp
    C = int(temp[0])
    D = int(temp[C+1])
    seq = temp[-1]
    for i in xrange(1, C+1):
        a = temp[i][0]
        b = temp[i][1]
        c = temp[i][2]
        combine[a] = b
        combine[b] = a
        nonbase[frozenset([a, b])] = c
    for i in xrange(C+2, C+2+D):
        a = temp[i][0]
        b = temp[i][1]
        oppose[a] = b
        oppose[b] = a
    ans = ""
    i = 0
    opposing = -1
    while i < len(seq):
        if opposing >= 0:
            if seq[i] == oppose[seq[opposing]]:
                ans = ""
                opposing = -1
                print "opposed"
                i += 1
                continue
        if seq[i] in combine:
            if (i + 1 < len(seq)) and (seq[i+1] == combine[seq[i]]):
                add = nonbase[frozenset([seq[i], seq[i+1]])]
                ans += add
                print "%s[%d] and %s[%d] combined into %s" % (seq[i], i, seq[i+1], i+1, add)
                i += 2
                continue
        if seq[i] in oppose:
            opposing = i
            print "opposing on %s[%d]" % (seq[i], i)
        ans += seq[i]
        i += 1
    
    finalAns = "["
    if len(ans) > 0: finalAns += ans[0]
    for i in xrange(1, len(ans)):
        finalAns += (", " + ans[i])
    finalAns += "]"
    print "Case #%d: %s" % (caseID, finalAns)
    fout.write("Case #%d: %s\n" % (caseID, finalAns))

fin.close()
fout.close()

#raw_input()
