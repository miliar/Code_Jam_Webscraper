import sys

def solve(cost, extra_rate, final_target, rate = 2, time = 0):
    t1 = (final_target / (rate + extra_rate)) + (cost / rate)
    t2 = final_target / rate
    if t1 >= t2:
        return t2 + time
    else:
        #print "bought farm"
        return solve(cost, extra_rate, final_target, rate + extra_rate, time + (cost / rate))

if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    t = int(raw_input())
    for i in range(1, t + 1):
        cost, extra_rate, final_target = map(float, raw_input().split(" "))
        print "Case #" + str(i) + ":", round(solve(cost, extra_rate, final_target), 7)
