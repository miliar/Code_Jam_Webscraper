inputfile = open("A-small-attempt6.in", "r")
#inputfile = open("input.txt", "r")
outputfile = open("output.txt", "w")
case_counter = 0
next(inputfile)
for line in inputfile:
    prev_val = 1
    curr_val = 0
#    print len(line)
    if len(line) > 2:
        case_counter += 1
        easyway = line.split()
        old_nti = 0
        nti = 0
        sval = 0
        sum_counter = 0
        checker = 0
#        print line
        for number in easyway[1]:
            if sval >= 1:
                prev_val = curr_val
            curr_val = number
            if prev_val == "0" and curr_val != "0":
                checker += 1
                old_nti = nti
                nti = sval - sum_counter
            sum_counter = sum_counter + int(number)
            sval += 1
        if checker >= 1:
            if old_nti > nti:
                nti = old_nti
        if nti < 0:
            nti = 0
            old_nti = 0
        outputfile.write("Case #" + str(case_counter) + ": " + str(nti) + "\n")
    else:
        continue
