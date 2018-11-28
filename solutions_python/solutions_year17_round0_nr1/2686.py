for c in xrange(1, int(raw_input()) + 1):
    ans = 0
    p_str, l = raw_input().split()
    l = int(l)
    p_list = [p for p in p_str]
    
    for i in xrange(len(p_list) - l + 1):
        if p_list[i] == '-':
            ans += 1
            for j in xrange(l):
                if p_list[i + j] == '-':
                    p_list[i + j] = '+'
                else:
                    p_list[i + j] = '-'

    for i in xrange(1, l + 1):
        if p_list[-i] == '-':
            ans = 'IMPOSSIBLE'
            break

    print "Case #%d: %s" % (c, ans)
