def solve():
    goal, otherHorses = map(int, input().split())
    horses = []
    for j in range(otherHorses):
        startpos, speed = map(int, input().split())
        horses.append((startpos, (goal - startpos) / speed))

    horses.sort(key = lambda x : x[0],reverse=True)
    maximumTime = -1
    while horses:
        pos, time = horses.pop()
        maximumTime = max(maximumTime, time)

    return goal / maximumTime 
T = int(input())
for i in range(1, T + 1):
    ans = "{0:.6f}".format(solve())
    print("Case #{}: {}".format(i, ans))