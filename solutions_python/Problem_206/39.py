import sys
sys.stdout = open('a_large.out', 'w')
sys.stdin  = open("a_large.in", 'r')
sys.setrecursionlimit(1500)

def algorithm(D, N, horses):
    max_arrival_time = 0
    for horse in horses:
        pos, speed = horse
        arrival_time = (D - pos) / float(speed)
        max_arrival_time = max(max_arrival_time, arrival_time)

    return float(D / max_arrival_time)





def solve():
    D, N = map(int, raw_input().split())
    horses = []
    for _ in range(N):
        horse = map(int, raw_input().split())
        # position, then speed
        horses.append(horse)
    return algorithm(D, N, horses)


T = int(raw_input())
for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)