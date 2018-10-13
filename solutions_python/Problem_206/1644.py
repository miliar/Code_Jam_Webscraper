import sys, functools
from math import floor, ceil

sys.stdin = open("A-small-attempt0.in", "r")
sys.stdout = open("sol", "w")

def finishing_time(D, horse):
    return (D - horse[0]) / horse[1]

def solve(D, N, horses):
    horses.sort(key=lambda x: x[0], reverse=True)

    horse = horses[0]
    time = finishing_time(D, horse)

    for i in range(1, N):
        horse = horses[i]

        if finishing_time(D, horse) > time:
            time = finishing_time(D, horse)
        else:
            meeting_point = ((horses[i-1][0] - horse[0]) / abs(horses[i-1][1] - horse[1])) * horse[1] + horse[0]
            if meeting_point >= D:
                time = finishing_time(D, horse)
            else:
                time = (meeting_point - horse[0]) / horse[1] + (D - meeting_point) / horses[i-1][1]

    return D / time

T = int(input())

for t in range(T):
    D, N = map(int, input().split())
    horses = []

    for n in range(N):
        horses.append(tuple(map(int, input().split())))

    sol = solve(D, N, horses)
    print("Case #" + str(t+1) + ":", "%.6f" % sol)