
from __future__ import division

T = int(raw_input())
for i in range(0, T):
    data = map(int, raw_input().split())
    D = data[0]
    N = data[1]

    time = 0
    for j in range(0, N):
        horse = map(int, raw_input().split())
        K = horse[0]
        S = horse[1]
        time = max(time, (D - K) / S)

    print("Case #%d: %f" % ((i+1), D/time))