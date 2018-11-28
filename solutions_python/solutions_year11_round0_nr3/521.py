import fileinput
from collections import defaultdict

def read_problem():
    f = fileinput.input()
    N = int(f.readline())
    for i in range(1, N+1):
        M = int(f.readline())
        L = map(int, f.readline().split())
        assert M == len(L)
        yield i, L

def solve(Candies):
    if reduce(lambda x,y: x^y, Candies) != 0:
        return "NO"
    Candies.sort()
    return sum(Candies[1:])

def main():
    for case, problem in read_problem():
        print "Case #%d:" % case, solve(problem)

if __name__ == '__main__':
    main()
