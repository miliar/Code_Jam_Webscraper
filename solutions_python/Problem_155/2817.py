__author__ = 'Tomasz'
import sys

test_cases = open(sys.argv[1], 'r').read().splitlines()

del test_cases[0]
case_no = 1
for case in test_cases:
    data = case.split()
    max_shyness = int(data[0])
    current_shyness_level = 0
    friends_needed = 0
    people_applouded = 0
    audience = data[1]
    for group in audience:
        if current_shyness_level > people_applouded:
            new_friends = current_shyness_level - people_applouded
            friends_needed += new_friends
            people_applouded += new_friends
        people_applouded += int(group)
        current_shyness_level += 1

    print "Case #{}: {}".format(case_no, friends_needed)
    case_no += 1