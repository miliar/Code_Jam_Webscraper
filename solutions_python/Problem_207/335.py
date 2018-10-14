
l_map = {
    0: 'R',
    2: 'Y',
    4: 'B'
}

def solve(unicorns):
    s_u = [[unicorns[i], i] for i in xrange(len(unicorns))]
    s_u.sort(reverse=True)

    first = s_u[0]
    seq = [l_map[first[1]],] * first[0]

    second = s_u[1]
    third = s_u[2]
    for i in xrange(first[0]):
        if second[0] > 0:
            second[0] -= 1
            seq.insert(i * 2 + 1, l_map[second[1]])
        else:
            if third[0] > 0:
                third[0] -= 1
                seq.insert(i * 2 + 1, l_map[third[1]])
            else:
                return False, ''
                

    # leftover thirds
    for i in xrange(third[0]):
        seq.insert(i * 3 + 1, l_map[third[1]])
    return True, ''.join(seq)





for case in xrange(input()):
    nums = map(int, raw_input().split(' '))[1:]
    result, string = solve(nums)
    if result:
        print "Case #%d: %s" % (case+1, string)
    else:
        print "Case #%d: IMPOSSIBLE" % (case + 1,)



