#!/usr/bin/python3

def solve():
    return True;


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    dest, n_horses = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    horses = []

    for mj in range(n_horses):
        dist, horse = [int(s) for s in input().split(" ")]
        horses.append((dist,horse))
    allgt = []
    for h in horses:
        gd = dest - h[0]
        gt = gd / h[1]
        allgt.append(gt)

    ans = dest / max(allgt)

    print("Case #{}: {}".format(i, str(ans)))