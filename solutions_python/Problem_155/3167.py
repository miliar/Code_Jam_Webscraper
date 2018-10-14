import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        test_cases = [l.strip().split(' ') for l in f.readlines()][1:]

    for test_num, (s_max, counts) in enumerate(test_cases):
        s_max = int(s_max)
        counts = map(int, list(counts))
        num_set = set()
        num_standing = 0
        num_friends = 0
        for i, count in enumerate(counts):
            if num_standing < i:
                num_friends += i - num_standing
                num_standing += i - num_standing
            num_standing += count
        print 'Case #%d: %d' % (test_num + 1, num_friends)
