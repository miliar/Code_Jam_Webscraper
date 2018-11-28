import sys

lines = sys.stdin.readlines()

i = 1

while i<len(lines):
    s = set()
    msg = lines[i].rstrip()
    for each in msg:
        s.add(each)
    #print len(s)
    maxbase = len(s)
    if maxbase == 1:
        maxbase = 2
    cost = maxbase ** (len(msg)-1)
    cands = range(len(s))
    cands.reverse()
    try:
        cands.remove(1)
    except:
        pass
    power = len(msg)-2
    index = 2
    prev = {}
    prev[msg[0]] = 1
    for x in xrange(1, len(msg)):
        c = msg[x]
        #print c
        if not prev.has_key(c):
            prev[c] = int(cands.pop())
        #print prev[c]
        #print "maxbase ", maxbase
        #print "power ", power
        cost += prev[c] * (maxbase ** power)
        power -= 1
    #print prev
    print "Case #"+str(i)+": "+str(cost)
    i += 1
