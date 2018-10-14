T = input()

def flip_char(c):
    return '-' if c == '+' else '+'

def flip(p, k, i):
    for j in xrange(i, i+k):
        p[j] = flip_char(p[j])

def solve(p, k):
    i = 0
    end = len(p)-k
    flip_count = 0
    while i < end:
        if p[i] == '-':
            flip(p, k, i)
            flip_count += 1
#            print p
        i += 1
    last_signs = set(p[end : len(p)])
    if len(last_signs) > 1:
        return 'IMPOSSIBLE'
    elif '+' in last_signs:
        return flip_count
    else:
        return flip_count + 1

for t in range(T):
    p, k = raw_input().split()
    p = list(p)
    k = int(k)
    ans = solve(p, k)
    print 'Case #{0}: {1}'.format(t+1, ans)
