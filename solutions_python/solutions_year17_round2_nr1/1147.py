import math

def solve(D, N, horses):
    speed = math.inf
    for horse in horses:
        speed = min(speed, horse[1]/(1 - horse[0]/D))
    return speed

cases = int(input())

for t in range(1, cases + 1):
    D, N = [int(s) for s in input().split(' ')]
    horses = []
    for i in range(1, N + 1):
        horse_pos, horse_speed = [float(s) for s in input().split(' ')]
        horses.append([horse_pos, horse_speed])
    answer = solve(D, N, horses)
    print("Case #{}: {}".format(t, answer))


