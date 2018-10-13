def TimeToGoal(current, rate, goal):
    return (goal - current) / rate

def RunTest(Current, R, C, F, X):
    ttg = 1.0
    ttgf = 0.0
    time = 0.0
    while ttg > ttgf:
        ttf = C / R
        ttg = TimeToGoal(Current, R, X)
        ttgf = ttf + TimeToGoal(Current, R + F, X)
        if ttgf < ttg:
            time += ttf
            R += F
    return time + ttg

def main():
    numTests = int(raw_input())
    for i in xrange(numTests):
        values = [float(c) for c in raw_input().split()]
        seconds = RunTest(0.0, 2.0, values[0], values[1], values[2])
        print "Case #" + str(i + 1) + ": " + str(seconds)
main()
