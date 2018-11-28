import fileinput
f = fileinput.input()

from collections import namedtuple

Stretch = namedtuple('Stretch', ['start', 'end'])


T = int(f.readline())
for case in range(1, T+1):
    A_C, A_J = (int(x) for x in f.readline().split())

    activities = list()

    for i in range(A_C+A_J):
        start, end = (int(x) for x in f.readline().split())
        activities.append(Stretch(start, end))

    total_activity_time = sum(i.end - i.start for i in activities)

    solution = 2
    if A_C == 2 or A_J == 2:
        gaps = [activities[1].end - activities[0].start, activities[0].end - activities[1].start]
        gaps = [s % 1440 for s in gaps]
        if any(s <= 720 for s in gaps):
            solution = 2
        else:
            solution = 4

    print(f"Case #{case}: {solution}")



