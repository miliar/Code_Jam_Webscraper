with open("A-small-attempt0.in", "r") as r:
    skipper = 0
    test_status = 0
    c1, c2, c3, check = ([], [], [], [])
    res = ''
    for idx, line in enumerate(r):
        line = line[:-1]
        if idx == 0:
            test_cases = int(line)
            test_case = 0
            if test_cases < 1 or test_cases > 100:
                print "Error: number of test cases invalid!"
                break
        elif (idx - 1) % 10 == 0:
            skipper = int(line)-1
            test_status = 1
            if skipper < 0 or skipper > 3:
                print "Error: invalid answer!"
                break
        elif (idx - 6) % 10 == 0:
            skipper = int(line)-1
            test_status = 2
            if skipper < 0 or skipper > 3:
                print "Error: invalid answer!"
                break
        else:
            check.extend(line.split(' '))
            if skipper > 0:
                skipper -= 1
            elif skipper == 0:
                skipper -= 1
                # end of 2nd set
                if test_status == 2:
                    c2 = [int(x) for x in line.split(' ')]
                    c3 = list(set(c1) & set(c2))
                    magic = len(c3)
                    test_case += 1
                    if magic == 1:
                        res = str(c3[0])
                    elif magic > 1:
                        res = 'Bad magician!'
                    else:
                        res = 'Volunteer cheated!'
                    test_status = 0
                elif test_status == 1:
                    c1 = [int(x) for x in line.split(' ')]
        if idx % 5 == 0 and idx > 0:
            if len(set(check)) != 16:
                print check
                print "Error: missing or dupe cards!"
                break
            elif not all(int(x) >= 1 and int(x) <= 16 for x in check):
                print "Error: invalid cards!"
                break
            elif idx % 10 == 0:
                print "Case #"+str(test_case)+": "+res
            check = []
        if test_cases == 0 and test_status:
            break
