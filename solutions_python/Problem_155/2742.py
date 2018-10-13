with open('standing-ovation-in.txt', 'r') as f:
    num_tests = int(f.readline())
    for case, line in enumerate(f.readlines(), start=1):
        s_max = int(line.split(' ')[0])
        digits = map(int, list(line.split(' ')[1].rstrip()))
        assert len(digits) == s_max + 1

        result = 0
        num_standing_people = digits[0]
        for level, digit in enumerate(digits[1:], start=1):
            while num_standing_people + result < level:
                result += 1
            num_standing_people += digit

        print "Case #%d: %d" % (case, result)

