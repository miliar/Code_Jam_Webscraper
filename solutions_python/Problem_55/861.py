

def roller_day(k, r, queue):
    idx=0
    money = 0
    while r:
        sum = 0
        lastIdx = idx
        while sum+queue[idx]<=k:
            sum += queue[idx]
            #money += queue[idx]
            idx = (idx+1)%len(queue)
            if idx==lastIdx:
                break
        money += sum
        r-=1
        #print "sum:%d, run: %d, idx: %d, mon:%d, queue:%s"%(sum, r, idx, money, queue)
    return money
#roller_day

import sys
if len(sys.argv)<2:
    print "%s <input>" % sys.argv[0]
    sys.exit(1)

input = file(sys.argv[1])
cases = int(input.readline().strip())
for case in range(cases):
    r, k, n = [int(x) for x in input.readline().strip().split()]
    people = [int(x) for x in input.readline().strip().split()]
    print "Case #%d: %d" % (case+1, roller_day(k, r, people))
