def flip(buf, s, e):
    for i in xrange(s, e + 1):
        buf[i] = not buf[i]

def findmin(s, k):
    count = 0
    buf = [False if c == '-' else True for c in s]
    for i in xrange(len(buf)):
        if buf[i] == False:
            if i + k <= len(s):
                count += 1
                flip(buf, i, i + k - 1)
            else:
                return "IMPOSSIBLE"
    return count




if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        s, k = raw_input().split(' ')
        res = findmin(s, int(k))
        print "Case #{}: {}".format(i, res)