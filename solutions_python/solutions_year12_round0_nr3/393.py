def num_of_recycled_pairs(a, b):
    pairs = set()
    for n in range(a, b):
        for m in recycled_numbers(n):
            if n < m <= b:
                pairs.add((n, m))
    return len(pairs)

def recycled_numbers(n):
    s = str(n)
    for i in range(1, len(s)):
        m = s[i:] + s[:i]
        #print n, m
        if m[0] != '0':
            yield int(m)

with open('/Users/vorushin/Downloads/C-large.in') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        a, b = [int(num) for num in f.readline().split()]
        print 'Case #%d: %d' % (i, num_of_recycled_pairs(a, b))
