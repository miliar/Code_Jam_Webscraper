def getn(s, k):
    i = 0
    n = len(s)
    res = 0
    while i + k <= n:
        if s[i] == '-':
            temp = ''.join(['+' if c == '-' else '-' for c in s[i:i+k]])
            s = s[:i]+ temp + s[i+k:]
            res += 1
        i += 1
    return res if s == '+' * n else "IMPOSSIBLE"

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t+1):
        s, k = raw_input().split(" ")
        print "Case #{}: {}".format(i, getn(s, int(k)))
