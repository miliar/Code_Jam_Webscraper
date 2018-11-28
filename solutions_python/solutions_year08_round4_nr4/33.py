def permute(a):
    if len(a) == 1: yield a
    b = sorted(a)
    for i in xrange(len(b)):
        for p in permute(b[:i] + b[i+1:]):
            yield [b[i]] + p

def solve(k, s):
    min_size = len(s)
    for b in permute(range(k)):
        t = []
        for i in xrange(len(s)//k):
            for j in xrange(k):
                t.append(s[i*k + b[j]])
        prev = ''
        size = 0
        for i in xrange(len(t)):
            if t[i] != prev: 
                prev = t[i]
                size += 1
            i += 1
        min_size = min(min_size, size)
    return min_size

for n in range(input()):
    k = input()
    s = raw_input()
    print("Case #%d: %d" %(n + 1, solve(k, s)))