import sys

t = int(raw_input())
for case in range(0, t):
    ans1 = int(raw_input())
    ord1 = map(lambda _: map(int, raw_input().split(' ')), range(0, 4))

    ans2 = int(raw_input())
    ord2 = map(lambda _: map(int, raw_input().split(' ')), range(0, 4))

    candids = set(ord1[ans1-1]).intersection(set(ord2[ans2-1]))

    sys.stdout.write("Case #%d: " % (case+1))
    if len(candids) == 1:
        print(candids.pop())
    elif len(candids) == 0:
        print("Volunteer cheated!")
    else:
        print("Bad magician!")
