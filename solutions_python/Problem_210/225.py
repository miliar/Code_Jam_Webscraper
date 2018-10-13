
fin = open("input.txt", "r")

tests_num = int(fin.readline())

for i in xrange(tests_num):
    [ac, aj] = [int(x) for x in fin.readline().split(" ")]
    cevents = []
    for _ in xrange(ac):
        cevents.append([int(x) for x in fin.readline().split(" ")])

    jevents = []
    for _ in xrange(aj):
        jevents.append([int(x) for x in fin.readline().split(" ")])

    if ac == aj or ac == 1 or aj == 1:
        print "Case #" + str(i + 1) + ": 2"
        continue
    cevents.sort(key=lambda x: x[0])
    jevents.sort(key=lambda x: x[0])

    if ac == 2:
        begin1 = cevents[0][0]
        end1 = cevents[0][1]
        begin2 = cevents[1][0]
        end2 = cevents[1][1]
        if begin2 - end1 >= 720 or 1440 - end2 + begin1 >= 720:
            print "Case #" + str(i + 1) + ": 2"
        else:
            print "Case #" + str(i + 1) + ": 4"
    else:
        begin1 = jevents[0][0]
        end1 = jevents[0][1]
        begin2 = jevents[1][0]
        end2 = jevents[1][1]
        if begin2 - end1 >= 720 or 1440 - end2 + begin1 >= 720:
            print "Case #" + str(i + 1) + ": 2"
        else:
            print "Case #" + str(i + 1) + ": 4"

fin.close()