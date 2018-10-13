from sys import stdin, stdout

def solve(cost, fps, goal):
    # print("Cost: {}".format(cost))
    # print("Fps: {}".format(fps))
    # print("goal: {}".format(goal))

    farms = 0
    cps = 2.0
    time = 0.0

    cur = goal / cps

    while True: # TODO some bound on farms
        next = time + goal / cps
        if next > cur:
            return cur
        else:
            cur = next
        time += cost / cps
        cps += fps
        farms += 1


def get_groups(s):
    groups = []
    cur = None
    cnt = 0
    for c in s:
        if cur is None:
            cur = c
            cnt = 1
        else:
            if cur == c:
                cnt += 1
            else:
                groups.append((cur, cnt))
                cur = c
                cnt = 1
    groups.append((cur, cnt))
    return groups

def solve(ls):
    FEGLA_WON = "Fegla Won"

    groupss = [get_groups(s) for s in ls]

    n = len(groupss[0])
    if any([len(g) != n for g in groupss]):
        return FEGLA_WON

    res = 0
    for i in range(n):
        curc = groupss[0][i][0]
        curcnt = 0
        for g in groupss:
            c, cnt = g[i]
            if curc != c:
                return FEGLA_WON
            curcnt += cnt
        mid = curcnt // len(ls)
        ans = 0
        mid1 = mid + 1
        ans1 = 0
        for g in groupss:
            _, cnt = g[i]
            ans += abs(cnt - mid)
            ans1 += abs(cnt - mid1)
        res += min(ans, ans1)
    return res



def main():
    lines = [l[:-1] for l in stdin.readlines()]

    t = int(lines[0])
    lines = lines[1:]

    for test in range(t):
        n = int(lines[0])
        ls = lines[1: 1 + n]
        lines = lines[1 + n:]

        print("Case #{}: {}".format(test + 1, solve(ls)))

main()

