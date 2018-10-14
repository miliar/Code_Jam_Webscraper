import sys
from collections import defaultdict
def getnum():
    return [int(x) for x in sys.stdin.readline().split()]

def getstr():
    return [str(x) for x in sys.stdin.readline().split()]

T, = getnum()

for t in range(T):
    row = getstr()
    comb = defaultdict(str)
    opp = defaultdict(list)
    #print row
    combnum = int(row[0])
    pos = 1
    for i in range(combnum):
        s = row[pos+i]
        comb[s[:2]] = s[2:3]
        comb[s[:2][::-1]] = s[2:3]
    #print comb
    pos += combnum
    oppnum = int(row[pos])
    pos += 1
    for i in range(oppnum):
        s = row[pos+i]
        opp[s[0:1]].append(s[1:2])
        opp[s[1:2]].append(s[0:1])
    #print opp
    pos += oppnum
    baselen = int(row[pos])
    pos += 1
    base = row[pos]
    buf = ""
    #print "base", base
    for i in range(len(base)):
        buf += base[i] # invoke
        #print "buf", buf
        #print buf[-2:]
        if len(buf) >= 2:
            # combine first
            if buf[-2:] in comb:
#                print "combine!", buf[-2:], comb[buf[-2:]]
                buf = buf[:-2] + comb[buf[-2:]]
            # oppose
            last = buf[-1]
            for j in range(len(opp[last])):
                if opp[last][j] in buf:
                    buf = ""
    print "Case #%d: %s" % (t+1, "[" + ", ".join(buf) + "]")
#    break
