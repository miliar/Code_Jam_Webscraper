import sys


sys.setrecursionlimit(1024)


def solve(line):
    people = [int(e) for e in line.split()[1]]
    def f(people, stand_up=0, si=1, add=0):
        if not people:
            return add
        stand_up += people[0]
        people = people[1:]
        if stand_up < si:
            add += 1
            stand_up += 1
        return f(people, stand_up, si+1, add)
    return f(people)


cases = int(sys.stdin.readline())
for case in range(1, cases+1):
    print 'Case #%d: %s' % (case, solve(sys.stdin.readline().strip()))
