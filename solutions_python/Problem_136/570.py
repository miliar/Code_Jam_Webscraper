import sys


def calculate(curr_total, rate, goal):
    return (goal - curr_total) / rate


def solve(C, F, X):
    cache = {}
    curr_total, rate = 0, 2
    t = calculate(curr_total, rate, X)

    while curr_total + C < X:
        if rate not in cache:
            cache[rate] = calculate(0, rate, C)

        new_t = t - calculate(curr_total, rate, X) + cache[rate] + \
                    calculate(curr_total, rate + F, X)
        
        if new_t < t:
            t = new_t
            rate += F
        else:
            break
    return t

def main():
    for tc in range(1, int(sys.stdin.readline()) + 1):
        C, F, X = [float(x) for x in sys.stdin.readline().split()]
        print("Case #%s: %.7f" % (tc, solve(C, F, X)))

if __name__ == '__main__':
    main()
