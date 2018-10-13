import heapq

def finddp(n, k):
    count = 0
    while True:
        low = (n + 1)/2 - 1
        if n % 2 == 0:
            high = low + 1
        else:
            high = low
        k -= 1
        if k == 0:
            return high, low
        if k == 1:
            k = 1
            n = high
        else:
            if k % 2 == 0:
                k  = k/2
                n = low
            else:
                k = k/2 + 1
                n = high
    return -1, -1

def find(n, k):
    if n == k:
        return (0, 0)
    count = 0
    q = []
    heapq.heappush(q, -n)
    res = None
    while count != k and len(q):
        n = heapq.heappop(q) * -1
        val = (n + 1)/2 - 1
        if val >= 0:
            if n % 2 == 0:
                res = (val + 1, val)
                heapq.heappush(q, (val + 1) * -1)
            else:
                res = (val, val)
                if val > 0:
                    heapq.heappush(q, val * -1)
            if val > 0:
                heapq.heappush(q, val * -1)
            count += 1
    return res

def calcls(a, s):
    count = 0
    i = s - 1
    while i > 0 and a[i] == 0:
        count += 1
        i -= 1
    return count

def calcrs(a, s, n):
    count = 0
    i = s + 1
    while i < n + 2 and a[i] == 0:
        count += 1
        i += 1
    return count

def findbruteforce(n, k):
    a = [0] * n
    a = [1] + a
    a.append(1)
    count = 0
    vals = [None] * (n + 2)
    res = None
    while count != k:
        for i in xrange(1, n + 2):
            if a[i] == 1:
                vals[i] = None
                continue
            ls = 0
            rs = 0
            ls = calcls(a, i)
            rs = calcrs(a, i, n)
            vals[i] = (ls, rs)

        # find max of min(ls,rs)
        maxcount = 0
        maxval = float('-inf')
        mintuples = []
        for i in xrange(1, n + 2):
            if vals[i] is None:
                continue
            t = vals[i]
            if min(t) >= maxval:
                maxval = min(t)
                if mintuples and min(mintuples[-1][1]) == maxval:
                    mintuples.append((i, t))
                else:
                    mintuples = [(i, t)]
                maxcount += 1
        if maxcount == 1:
            res = mintuples[0]
            vals[res[0]] = res[1]
            a[res[0]] = 1
        else:
            # find max of mintuples
            maxval = float('-inf')
            maxtuples = []
            for i in xrange(len(mintuples)):
                idx, t = mintuples[i]
                if max(t) >= maxval:
                    maxval = max(t)
                    if maxtuples and max(maxtuples[-1][1]) == maxval:
                        maxtuples.append((idx, t))
                    else:
                        maxtuples = [(idx, t)]
            res = maxtuples[0]
            vals[res[0]] = res[1]
            a[res[0]] = 1
        count += 1
    return max(res[1]), min(res[1])





if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = [int(c) for c in raw_input().split(' ')]
        resdp = finddp(n , k)
        #res = find(n, k)
        #resbf = findbruteforce(n , k)
        print "Case #{}: {} {}".format(i, resdp[0], resdp[1])