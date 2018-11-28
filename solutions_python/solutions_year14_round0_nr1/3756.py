T = int(raw_input())
for item in xrange(T):
    in1 = int(raw_input())
    for i in xrange(4):
        inp = raw_input()
        if i == (in1 - 1):
            suspects1 = map(int, inp.split())
    in2 = int(raw_input())
    for i in xrange(4):
        inp = raw_input()
        if i == (in2 - 1):
            suspects2 = map(int, inp.split())

    result = list(set(suspects1) & set(suspects2))

    if len(result) == 1:
        print "Case #" + str(item + 1) + ": " + str(result[0])
    else:
        if len(result) == 0:
            print "Case #" + str(item + 1) + ": " + "Volunteer cheated!"
        else:
            print "Case #" + str(item + 1) + ": " + "Bad magician!"

