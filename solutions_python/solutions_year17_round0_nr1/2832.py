def flipK(l, start, k):
    if start + k > len(l):
        return None
    for i in range(start, start+k):
        l[i] = '-' if l[i] == '+' else '+'
    return l

def count(l, k):
    flips = 0
    for i, val in enumerate(l):
        if val == '-':
            l = flipK(l, i, k)
            # print l
            if l == None:
                return 'IMPOSSIBLE'
            flips += 1
    return str(flips)

cases = int(raw_input())
for case in range(1, cases + 1):
    l, k = tuple(raw_input().split(' '))
    val = count(list(l), int(k))
    print('Case #%d: %s' % (case, val))
