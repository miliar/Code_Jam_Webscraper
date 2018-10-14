import sys

def solve(C, F, X):
    rate = 2
    if X < C:
        return X / rate
    t = C / rate
    while True:
        time_until_amortized = C / F
        time_until_finished = (X - C) / rate
        if time_until_amortized < time_until_finished:
            rate += F
            t += C / rate
        else:
            return t + time_until_finished

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        data = []
        C, F, X = map(float, sys.stdin.readline().split())
        result = solve(C, F, X)
        print "Case #%d: %s" % (t + 1, result)

if __name__ == '__main__':
    main()
