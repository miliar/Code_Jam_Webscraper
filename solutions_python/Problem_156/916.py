#!/usr/bin/env python
# >

import sys



def eats(plates):
    for i in range(0, len(plates)):
        if plates[i] == 0:
            pass ;
        else:
            plates[i] -= 1
    return plates

def divided_two(plates):
    splitter = max(plates)
    plates.remove(splitter)
    if splitter % 2:
        plates.append(splitter/2)
        plates.append(splitter/2 +1)
    else:
        plates.append(splitter/2)
        plates.append(splitter/2)
    return plates

def divided_three(plates):
    splitter = max(plates)
    plates.remove(splitter)
    if splitter % 3:
        plates.append(splitter / 3 + (splitter % 3))
        plates.append(splitter / 3 * 2)
    elif splitter % 3 == 0:
        plates.append(splitter / 3)
        plates.append(splitter / 3 * 2)
    return plates

def work(plates, turn):
    results.append(max(plates)+turn)
#    print "**", turn, plates, min(results)
    if max(plates) > 3:
        tmp1 = divided_two(plates[:])
#        print "/2", turn, plates, min(results)

        work(tmp1, turn+1)
        tmp2 = divided_three(plates[:])
#        print "/3", turn, plates, min(results)
        work(tmp2, turn+1)
        tmp3 = eats(plates[:])
#        print "eats", turn, plates, min(results)
        work(tmp3, turn+1)
    return ;

flag = 0
nbr_plates = 0
for line in file(sys.argv[1]):
    if flag == 0:
        ntests = int(line)
        flag = 1
        continue ;
    result = 0
    if nbr_plates == 0:
        nbr_plates = int(line[:-1])
        continue
    else:
        results = []
        plates = [int(n) for n in line[:-1].split(" ")]
        work(plates, 0)
        print "Case #%d: %d" % (flag, min(results))
        nbr_plates = 0
        flag += 1
