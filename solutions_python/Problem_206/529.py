def meetpoint(horse0, horse1):
    if horse1[1] == horse0[1]:
        return float("inf")
    t = (horse0[0] - horse1[0]) / (horse1[1] - horse0[1])
    return horse0[0] + horse0[1] * t

T = int(input())
for t in range(1, T+1):
    D, N = [int(_) for _ in input().split(" ")]
    horse = []
    for n in range(N):
        K, S = [int(_) for _ in input().split(" ")]
        horse.append((K, S, (D-K)/S))
    
    maxspeed = float("inf")
    for i in range(len(horse)):
        horse1 = horse[i]
        time = (D-horse1[0])/horse1[1]
        maxspeed = min(maxspeed, D/time)
        for j in range(i+1,len(horse)):
            horse2 = horse[j]
            if meetpoint(horse1, horse2) < D:
                time = min((D-horse1[0])/horse1[1], (D-horse2[0])/horse2[1])
                maxspeed = min(maxspeed, D/time)
                # maxspeed = min(maxspeed, min(horse1[1], horse2[1]))
    print("Case #{}: {}".format(t, maxspeed))