import sys

def elapse(cookies, goal, cps, current_time):
    return ((goal - cookies) / cps) + current_time


T = int(sys.stdin.readline())
for testcase in range(T):
    # per testcase
    c,f,x = map(float, sys.stdin.readline().split())

    cps = 2
    time = elapse(0, min(c,x), cps, 0)
    cookies = c
    while cookies < x:
        time_wait = elapse(cookies, x, cps, time)
        time_buy = elapse(cookies - c, x, cps + f, time)
        if time_wait <= time_buy:
            time = time_wait
            break
        else:
            cps += f
            goal = min(c,x)
            time = elapse(cookies - c, goal, cps, time)
            cookies = goal

    print "Case #" + str(testcase + 1) + ": " + ("%.7f" % time)



