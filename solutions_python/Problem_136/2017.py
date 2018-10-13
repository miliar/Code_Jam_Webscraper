from sys import stdin, stdout

def compute():
    C, F, X = map(float, stdin.readline().split(" "))
    # C is cost of farm
    # F is payback per sec from farm
    # X is goal

    # could use DP or shortest path
    # could be lazy and work with #farms

    timeToFarms = [0]
    rate = 2.0
    best = 1E12
    farms = 0
    while True:
        time = 0
        
        if farms:
            rate = 2.0 + (farms - 1) * F
            timeToFarms.append(timeToFarms[-1] + C / rate)
            rate += F

        time = timeToFarms[-1] + X / rate

        if time < best:
            best = time
        else:
            return "%.7f"%best

        farms += 1


T = int(stdin.readline())
for t in range(T):
    ans = compute()

    stdout.write("Case #%d: %s\n"%(t+1, ans))


