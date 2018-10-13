#!/usr/bin/python

def parse():
    return int(raw_input())

def solve(N):
    curr = N
    while curr > 0:
        digits = map(int, list(str(curr)))
        if sorted(digits) == digits:
            return curr
        curr -= 1
    return 0

def main():
    for i in range(int(raw_input())):
        N = parse()
        result = solve(N)
        print 'Case #%s: %s' % (i+1, result)

if __name__ == "__main__":
    main()
