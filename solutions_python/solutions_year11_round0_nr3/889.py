import sys
import math
import itertools

def wrongAdd(seq):
    return reduce(lambda x,y:x^y, seq, 0)

l = sys.stdin.readline()
T = int(l.strip())
##print "T = %d" %(T)
cnt = 0
for t in range(T):
    cnt += 1
    N = int(sys.stdin.readline().strip())
##    print "N = %d" %(N)
    d = [int(c) for c in sys.stdin.readline().strip().split(" ")]
    d.sort()
##    print d

    sumA = 0
    sumB = 0
    maxSum = 0
    for n in range(1, int(math.ceil(N / 2.0)) + 1):
        comb = itertools.combinations(range(N), n)
##        print comb
        while (1):
            try:
                InIndex = comb.next()
                NotInIndex = filter(lambda x:x not in InIndex, range(N))
##                print InIndex, NotInIndex
                list1 = [d[i] for i in InIndex]
                list2 = [d[i] for i in NotInIndex]
                sumA = wrongAdd(list1)
                sumB = wrongAdd(list2)
                if sumA == sumB:
                    sumA = sum(list1)
                    sumB = sum(list2)
                    maxAB = max(sumA, sumB)
                    if maxAB > maxSum:
                        maxSum = maxAB
                    break
            except StopIteration:
                break
            
    if maxSum == 0:
        print "Case #%d: NO" %(cnt)
    else:
        print "Case #%d: %d" %(cnt, maxSum)
