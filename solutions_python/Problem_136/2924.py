import sys

#def solve(c, f, x, rate = 2):
#    wait = x / rate
#    time_to_build = c / rate
#    new_rate = rate + f
#    build = time_to_build + (x / new_rate)
#    if wait >= build :
#        return time_to_build + solve(c, f, x, new_rate)
#    return wait

def solve(c, f, x, rate = 2):
    time = 0
    wait = x / rate
    time_to_build = c / rate
    new_rate = rate + f
    build = time_to_build + (x / new_rate)
    while wait >= build :
        time = time + time_to_build
        rate = new_rate
        wait = x / rate
        time_to_build = c / rate
        new_rate = rate + f
        build = time_to_build + (x / new_rate)
    return wait + time

numcases = int(sys.stdin.readline())
for casenum in range(1, numcases+1):
    data = sys.stdin.readline().strip().split()
    c = float(data[0])
    f = float(data[1])
    x = float(data[2])
    print("Case #{}: {}".format(casenum, solve(c, f, x)))