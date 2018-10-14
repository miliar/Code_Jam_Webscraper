import sys

def swap_state(state):
    if state == '+':
        return '-'
    return '+'

def sol(s, k):
    s = list(s)
    k = int(k)
    count = 0
    state = '+'
    state_count = 0
    pos = 0
    while pos < len(s) - k + 1:
        if s[pos] != '+':
            count += 1
            for i in range(k):
                s[pos + i] = swap_state(s[pos + i])
        pos += 1
    while pos < len(s):
        if s[pos] != '+':
            count = 'IMPOSSIBLE'
        pos += 1
    return count

def reader(filename):
    ret = []
    with open(filename) as f:
        t = int(f.readline())
        for _ in range(t):
            ret.append(f.readline().split(' '))

    return ret

data = reader(sys.argv[1])
for i in range(len(data)):
    out = sol(data[i][0], data[i][1])
    print "Case #%d: %s" % (i+1, out)
