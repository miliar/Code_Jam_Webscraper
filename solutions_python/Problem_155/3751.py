__author__ = 'wangguoxi'

number_of_testcases = int(raw_input())

for each in range(1, number_of_testcases+1):
    number_of_levels, people_string = raw_input().split()
    people_clapped = int(people_string[0])
    people_added = 0
    for level in range(1, int(number_of_levels) + 1):
        if people_clapped >= level:
            people_clapped += int(people_string[level])
        else:
            if people_string[level] == '0':
                continue
            else:
                people_added += (level - people_clapped)
                people_clapped += people_added
                people_clapped += int(people_string[level])
    print "Case #" + str(each) + ": " + str(people_added)

