import sys
test_cases = open(sys.argv[1], 'r')
num_cases = test_cases.readline()
case_num = 1
for test in test_cases:
    test = test.strip().split(" ")
    max_shy = int(test[0])
    audience = map(int, list(test[1]))
    added_friends = 0
    total_audience = 0
    for shyness in range (0, max_shy + 1):
        if audience[shyness] and total_audience < shyness:
            needed_members = shyness - total_audience
            total_audience += needed_members
            added_friends += needed_members
        total_audience += audience[shyness]

    print "Case #{}: {}".format(case_num, added_friends)
    case_num += 1

test_cases.close()