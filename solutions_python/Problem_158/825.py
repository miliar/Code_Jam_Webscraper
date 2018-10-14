__author__ = 'valeria'

__author__ = 'valeria'

from math import ceil, floor

def get_test():
    l = input().split()
    l = [int(x) for x in l]
    return l

def get_winner(test):
    x = test[0]
    r = test[1]
    c = test[2]
    if x > r * c:
        return "RICHARD"
    if (r * c) % x != 0:
        return "RICHARD"
    if (r < x) and (c < x):
        return "RICHARD"
    if (r < x - 1) or (c < x-1):
        return "RICHARD"
    return "GABRIEL"


def get_tests():
    n = int(input())
    tests = []
    for i in range(n):
        tests.append(get_test())
    return tests

def main():
    tests = get_tests()
    for index, test in enumerate(tests):
       print("Case #{}: {}".format(index + 1, get_winner(test)))



if __name__ == '__main__':
    main()
