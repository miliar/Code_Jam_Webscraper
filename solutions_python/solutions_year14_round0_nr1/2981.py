input_file = open("in", "r")
output_file = open("out", "w")

tests = int(input_file.readline())
for test in xrange(tests):
    ans1 = int(input_file.readline()) - 1
    a = [[] * 4] * 4
    for i in xrange(4):
        a[i] = map(int, input_file.readline().split(" "))

    ans2 = int(input_file.readline()) - 1
    b = [[] * 4] * 4
    for i in xrange(4):
        b[i] = map(int, input_file.readline().split(" "))

    was = False
    fail = False
    ans = 0
    for i in xrange(4):
        if b[ans2][i] in a[ans1]:
            if was:
                fail = True
                break
            was = True
            ans = b[ans2][i]

    if not was:
        output_file.write("Case #%d: Volunteer cheated!\n" % (test + 1))
    else:
        if fail:
            output_file.write("Case #%d: Bad magician!\n" % (test + 1))
        else:
            output_file.write("Case #%d: %s\n" % (test + 1, str(ans)))
