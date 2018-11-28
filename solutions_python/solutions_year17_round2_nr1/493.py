def solve(d, horses):
    time = 0
    for i in range(len(horses)):
        horse = horses[i]
        pos = horse[0]
        speed = horse[1]
        time = max(time, ((d-pos)*1.0)/speed)
    return d/time

t = int(input())
for i in range(1,t+1):
    d, n = [int(x) for x in input().split(" ")]
    horses = []
    for j in range(n):
        horses += [[int(x) for x in input().split(" ")]]
    print("Case #" + str(i) + ": " + str(solve(d, horses)))
