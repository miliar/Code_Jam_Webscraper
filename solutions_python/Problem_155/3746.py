test_cases = int(raw_input())

for test_case in range(test_cases):

    line = raw_input().split(' ')
    s_max = int(line[0])
    ss = [int(x) for x in line[1]]
    ss.reverse()
    min_invite = 0

    for i, s in enumerate(ss):
        j = s_max - i
        needed = max(0, j - sum(ss[i+1:]))
        min_invite = max(needed, min_invite)

    print "Case #{0}: {1}".format(test_case + 1, min_invite)
