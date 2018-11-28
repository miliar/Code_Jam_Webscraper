def solve():
    f = open("../B-large.in", "r")
    T = int(f.readline())
    out = open("../output.txt", "w")

    for case in range(T):
        C, F, X = map(float, f.readline().split())

        timePassed = 0.0
        rate = 2.0
        count = 1

        while X / rate > C / rate + X / (rate + F):
            timePassed += C / rate
            rate += F
            count += 1

        print("case: %d, count: %d" % (case + 1, count - 1))
        # timePassed = 0.0
        # rate = 2.0
        # count = 1
        #
        # while count < 700:
        #     timePassed += C / rate
        #     rate += F
        #     count += 1
        #     print("%f, %f" % (X / rate, C / rate + X / (rate + F)))

        #print("Case #%d: %.7f\n" % (case + 1, timePassed + X / rate))
        out.write("Case #%d: %.7f\n" % (case + 1, timePassed + X / rate))


solve()
