open_file = open('A-small-attempt1.in', 'r')
write_file = open('A-small-attempt1.out', 'w')

number_of_test_cases = int(open_file.readline().strip())

for test_case_number_from_zero in xrange(number_of_test_cases):
    line = open_file.readline().strip().split()
    # Smax = int(line[0])
    # shyness level from zero to Smax
    stand_up_count = 0
    invite_count = 0

    for shyness_level, this_level_people_count in enumerate(line[1]):
        this_level_people_count = int(this_level_people_count)
        if this_level_people_count > 0 and stand_up_count < shyness_level:
            invite_count += shyness_level - stand_up_count
            stand_up_count += invite_count
            # print shyness_level, this_level_people_count, invite_count, stand_up_count
        stand_up_count += this_level_people_count

    s = "Case #%d: %s\n" % (test_case_number_from_zero+1, invite_count)
    print s
    write_file.write(s)