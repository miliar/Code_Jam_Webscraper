num_test_cases = int(raw_input())
for test_case in range(num_test_cases):
    line = raw_input()
    audience_str = line.split()[1]
    num_invited = 0
    num_standing = 0
    for i in range(len(audience_str)):
        if num_standing >= i:
            num_standing += int(audience_str[i])
        else:
            num_invited += i - num_standing
            num_standing = i + int(audience_str[i])
    print "Case #%s: %d" % (test_case + 1, num_invited)
