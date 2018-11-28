import sys

def calculate(i, d):
    res = 0
    if d == 'l':
        i -= 1
        while i > 0:
            stall = stall_config[i]
            if stall:
                return res
            else:
                res += 1
                i -= 1
    else:
        i += 1
        while i < n+1:
            stall = stall_config[i]
            if stall:
                return res
            else:
                res += 1
                i += 1
    return res

t = int(raw_input())

for i in xrange(t):
    n, k = map(int, raw_input().split())

    stall_config = [1] + [0] * n + [1]
    for j in xrange(k):
        min_max = -sys.maxint
        max_max = -sys.maxint
        stall_max = stall_config.index(0)

        res_min, res_max = 0, 0

        for stall_index in xrange(stall_max, n+1):
            stall = stall_config[stall_index]

            if not stall:
                ls = calculate(stall_index, 'l')
                rs = calculate(stall_index, 'r')
                # print 'LS RS:', stall_index, ls, rs
                minimum = min(ls, rs)
                maximum = max(ls, rs)
                if minimum > min_max:
                    min_max = minimum
                    max_max = maximum
                    stall_max = stall_index
                    res_min, res_max = minimum, maximum
                elif minimum == min_max and maximum > max_max:
                    max_max = maximum
                    stall_max = stall_index
                    res_min, res_max = minimum, maximum

        stall_config[stall_max] = 1
    # print stall_config

    print 'Case #%d: %d %d' % (i+1, res_max, res_min)
