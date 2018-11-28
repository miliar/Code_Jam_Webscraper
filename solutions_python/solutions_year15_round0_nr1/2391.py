def find_min_aud(max_s, s):
    ss = list(s)
    count = 0
    aud = 0

    for i in xrange(max_s+1):
        if count < i:
            aud += i-count
            count = i

        count += int(ss[i])
    return aud


if __name__ == '__main__':
    import sys
    import os
    if len(sys.argv) != 2:
        print 'Wrong input num'
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print 'Cannot find file'
        sys.exit(1)

    with open(file_path) as f:
        case_num = int(f.readline())

        for i in xrange(case_num):
            
            max_s, s = f.readline().split()

            ans = find_min_aud(int(max_s), s)

            print "Case #%d: %d" % (i+1, ans)



