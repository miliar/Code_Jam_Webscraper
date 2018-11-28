import operator
fin = open('B-small-attempt2.in', 'r')
fout = open('output.out', 'w')
tcs = int(fin.readline())
for tc in range(0, tcs):
    inptemp = fin.readline().split(' ')
    ac = int(inptemp[0])
    aj = int(inptemp[1])
    acs = list()
    ajs = list()
    for i in range(0, ac):
        acinp = fin.readline().split(' ')
        acs.append([int(acinp[0]), int(acinp[1])])
    for i in range(0, aj):
        ajinp = fin.readline().split(' ')
        ajs.append([int(ajinp[0]), int(ajinp[1])])
    
    acs.sort(key=operator.itemgetter(0))
    ajs.sort(key=operator.itemgetter(0))

    result = -1
    if ac == 2 and aj == 0:
        time1 = acs[1][1] - acs[0][0]
        time2 = acs[1][0] - acs[0][1]
        print("time1, 2",time1, time2)
        if time1 <= 720 or time2 >= 720:
            result = 2
        else:
            result = 4
    if ac == 0 and aj == 2:
        time1 = ajs[1][1] - ajs[0][0]
        time2 = ajs[1][0] - ajs[0][1]
        print("time1, 2", time1, time2)
        if time1 <= 720 or time2 >= 720:
            result = 2
        else:
            result = 4
    if ac == 1 and aj == 0:
        result = 2
    if ac == 0 and aj == 1:
        result = 2
    if ac == 1 and aj == 1:
        result = 2

    
    print("Case #%d: %d" %(tc+1, result))
    fout.write("Case #%d: %d\n" %(tc+1, result))
fin.close()
fout.close()
