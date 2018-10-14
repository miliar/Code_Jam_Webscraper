def solve():
    N = int(input())
    m = map(int, raw_input().split())
    case_1, case_2, max_diff = 0, 0, 0
    for i in xrange(1, len(m)):
        if m[i-1] - m[i] > 0:
            case_1 += m[i-1] - m[i]
    
    for i in xrange(1, len(m)):
        max_diff = max(max_diff, m[i-1] - m[i])
    
    for i in xrange(len(m)-1):
        case_2 += min(max_diff, m[i])

    return [case_1, case_2]

T = input()
for i in xrange(T):
    ans = solve()
    print 'Case #%d: %s %s' % (i + 1, ans[0], ans[1])
