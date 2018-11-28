import sys

def read():
    return sys.stdin.readline().split(" ")

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solve_case():
    times = map(int, read()[1:])

    step = abs(times[0] - times[1])
    for i in range(1, len(times) - 1):
        step = gcd(step, abs(times[i] - times[i + 1]))

    print (step - times[0]) % step


def main():
    test_cases, = map(int, read())
    for case in range(1, test_cases + 1):
        print ("Case #%d:" % case),
        solve_case()

if __name__ == "__main__":
    main()


