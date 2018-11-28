input_file = open("in", "r")
output_file = open("out", "w")

tests = int(input_file.readline())
for test in xrange(tests):
    C, F, X = map(float, input_file.readline().split(" "))
    ans = 2e9
    for count_buys in xrange(10000):
        prev_ans = ans
        ans = 0.0

        f = 2
        for i in xrange(count_buys):
            ans += C / f
            f += F

        ans += X / f
        if ans >= prev_ans:
            ans = prev_ans
            print test + 1, count_buys
            if count_buys == 999:
                print '--------------------------------------------'
            break

    output_file.write("Case #%d: %.6lf\n" % (test + 1, ans))
