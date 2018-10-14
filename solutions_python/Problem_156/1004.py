import sys

from heapq import heappush, heappop

class MaxHeap:

    l = None

    def __init__(self):
        self.l = []
        pass

    def __init__(self, arr):
        self.l = []
        for x in arr:
            self.push(x)

    def push(self, x):
        heappush(self.l, -x)

    def pop(self):
        return -heappop(self.l)

    def peek(self):
        x = heappop(self.l)
        heappush(self.l, x)
        return -x

    def count(self, x):
        return self.l.count(x)


def getMinutes(vals, use963=True):
    h = MaxHeap(vals)

    maxMinutes = max(vals)
    minMinutes = maxMinutes


    minutes = 0
    while minutes <= maxMinutes:
        # Get the minimum of using the special method now and then eating the rest OR eating the rest immediately
        #print "minutes=%d, minMinutes=%d, minutes+h.peek()=%d" % (minutes, minMinutes, minutes+h.peek())
        minMinutes = min(minMinutes, minutes + h.peek())

        x = h.pop()

        if x == 9:
            if use963:
                a, b = 6, 3
            else:
                a, b = 5, 4
        else:
            a,b = x/2, (x%2) + x/2
        h.push(a)
        h.push(b)

        minutes += 1

        #print "minutes=%d, minMinutes=%d, minutes+h.peek()=%d" % (minutes, minMinutes, minutes+h.peek())
        minMinutes = min(minMinutes, minutes + h.peek())

    return minMinutes


for tc in range(1, 1 + int(sys.stdin.readline())):
    line = sys.stdin.readline()
    n = int(line)

    vals = sys.stdin.readline().strip().split(" ")
    vals = map(int, vals)

    #print n,vals

    vals1 = [x for x in vals]
    vals2 = [x for x in vals]
    minutes1 = getMinutes(vals1, use963=True)
    minutes2 = getMinutes(vals2, use963=False)
    minutes = min(minutes1, minutes2)

    print "Case #%d: %d" % (tc, minutes)
    #print ""

