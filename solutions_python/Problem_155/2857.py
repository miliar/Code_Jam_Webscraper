with open('A-large.in', 'r') as infile:
    number_of_test_cases = infile.readline()

    for test_case, line in enumerate(infile, start=1):
        max_shyness, people = line.split(' ')
        people = [int(p) for p in people.strip()]

        # your friends might as well all have shyness level 0
        num_friends_to_invite = 0

        num_standing = 0
        for level, person in enumerate(people):
            while num_standing < level:
                num_friends_to_invite += 1
                num_standing += 1
            num_standing += person

        print "Case #%d: %d" % (test_case, num_friends_to_invite)
        
        
  