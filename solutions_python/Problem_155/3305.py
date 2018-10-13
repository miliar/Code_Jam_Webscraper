def test_case(case_num):
    _, shyness_str = raw_input().rstrip().split()
    to_invite = 0
    standing = 0
    for shyness, count_str in enumerate(shyness_str):
        count = int(count_str)
        if count == 0:
            continue
        if standing < shyness:
            invited = shyness - standing
            to_invite += invited
            standing += invited
        standing += count
    print 'Case #{}: {}'.format(case_num, to_invite)

T = int(raw_input())
for i in xrange(T):
    test_case(i + 1)