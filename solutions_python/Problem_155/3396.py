f = open("C:\Users\Adam\Downloads\A-large.in")

case = 0
for line in f:
    line = line.strip('\n')
    line = line[line.find(" ")+1:]
    case += 1
    complete = 0
    friends = 0
    if case > 1:
        while complete == 0:
            ppl_0 = int(line[0])
            total_stand = 0 + ppl_0 + friends

            desc = line[1:]
            total_ppl = 0 + ppl_0 + friends
            for a in desc:
                total_ppl += int(a)


            level = 0
            for d in desc:
                level += 1
                if total_stand >= level:
                    total_stand += int(d)

            if total_stand == total_ppl:
                complete += 1
                print "Case #" + str(case-1) + ": " + str(friends)

            friends += 1
