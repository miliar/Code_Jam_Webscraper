from heapq import heappush, heappop


def stalls(n, k):
    if n == k:
        return 0, 0
    spaces = [-n]
    for x in range(k):
        max_space = -heappop(spaces)
        if max_space % 2:
            aux = [max_space / 2, max_space / 2]
        else:
            aux = [max_space / 2, (max_space / 2) - 1]
        if x < k - 1:
            for a in aux:
                heappush(spaces, -a)
        else:
            return aux


def main():
    t = int(raw_input().strip())
    for i in xrange(t):
        n, k = map(int, raw_input().strip().split())
        ans = stalls(n, k)
        print "Case #%s: %s" % (i + 1, ' '.join(map(str, ans)))

if __name__ == '__main__':
    main()
