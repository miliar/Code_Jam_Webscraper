filename = 'large.txt'
number_of_cases = None
case = 0


with open(filename) as f:
    for line in f:
        to_add = 0
        if not number_of_cases:
            number_of_cases = line.rstrip('\n')
            continue
        case = case + 1
        (max_shy, current_line) = line.rstrip('\n').split(" ")
        current_line = list(current_line)

        clapping = 0
        #print "Case #%d: %d" % (case, to_add)
        for level, number_of_people in enumerate(current_line):
            #print "Level %d number of people %s clapping %d" % (level, number_of_people, clapping)

            if int(number_of_people) > 0 and clapping < level:
                to_add = to_add + level - clapping
                #print "  adding %d" % to_add
                clapping = clapping + (level - clapping)

            clapping = clapping + int(number_of_people)
            #print "  inc clapping %s" % number_of_people

        print "Case #%d: %d" % (case, to_add)

