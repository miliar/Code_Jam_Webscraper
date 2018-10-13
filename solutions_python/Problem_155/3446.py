f = open('out.txt', 'w')

cases = int( raw_input() )

for case in range(cases):
    
    levels = [int(i) for i in str( raw_input() ).replace(" ", "")]
    levels.pop(0)

    
    number_of_guests_needed = 0
    number_of_guests_standing = 0

    do_guests_count = 0
    current_shyness = 0
    for level in levels:
        if level != 0:
            if number_of_guests_standing < current_shyness:
                number_of_guests_needed = number_of_guests_needed + current_shyness - number_of_guests_standing
                number_of_guests_standing = number_of_guests_standing + number_of_guests_needed
            number_of_guests_standing = number_of_guests_standing + level
        current_shyness = current_shyness + 1

    answer = number_of_guests_needed
    if answer < 0:
        answer = 0
    
    print "Case #" + str(case + 1) + ": " + str(answer)
    print >> f, "Case #" + str(case + 1) + ": " + str(answer)

f.close()
