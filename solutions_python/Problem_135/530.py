__author__ = 'robertking'

from sys import stdin

data = (line for line in stdin.read().splitlines())

def get_m():
    return map(tuple, [
        [],
        map(int, next(data).split()),
        map(int, next(data).split()),
        map(int, next(data).split()),
        map(int, next(data).split())
    ])

T = int(next(data))
for case in range(1, T + 1):
    ans1 = int(next(data))
    m1 = set(get_m()[ans1])
    ans2 = int(next(data))
    m2 = set(get_m()[ans2])
    intersection = m1 & m2
    if intersection:
        if len(intersection) == 1:
            ans = str(next(iter(intersection)))
        else:
            ans = "Bad magician!"
    else:
        ans = "Volunteer cheated!"
    print "Case #%d: %s" % (case, ans)

