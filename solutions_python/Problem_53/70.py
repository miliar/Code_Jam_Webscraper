import sys

def read():
    return sys.stdin.readline().split(" ")

def solve_case():
    n, k = map(int, read())

    if k % (2**n) == (2**n - 1):
        print "ON"
    else:
        print "OFF"

def main():
    test_cases, = map(int, read())
    for case in range(1, test_cases + 1):
        print ("Case #%d:" % case),
        solve_case()

if __name__ == "__main__":
    main()

