import sys

for tc in xrange(1, int(raw_input())+1):
    sys.stdout.write("Case #")
    print tc,
    sys.stdout.write(": ")
    line1 = raw_input()
    line2 =	raw_input()
    line1 = line1.split()
    A = int(line1[0])
    B = int(line1[1])
    remain_keystroke = B - A
    prob = line2.split()
    prob = [float(x) for x in prob]

    goodstate = remain_keystroke + 1
    badstate = remain_keystroke + B + 2
    last = B + 2.0000
    ans = last

    for i in xrange(A+1):
        if ( goodstate > last ):
            break

        correct_p = 1.0000
        for e in prob:
            correct_p *= e
        if prob:
            prob.pop()

        expected_val = goodstate * correct_p + badstate * (1.0000-correct_p)

        if (expected_val < ans):
            ans = expected_val
        goodstate += 2
        badstate += 2

    print ans
