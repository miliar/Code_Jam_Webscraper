for trial in range(int(raw_input())):
    N = int(raw_input())
    C = map(int, raw_input().split())
    r = reduce(int.__xor__, C) and 'NO' or sum(C)-min(C)
    print 'Case #%d: %s' % (trial+1, r)

