import pdb
def speed(d, n, horse):
    slowest = horse[0][1]
    time = 0
    for i in horse:
        horse_time = (d - int(i[0])) / int(i[1])
        if horse_time >= time:
            time = horse_time

    return str(d / time)

test_cases = int(input())
cases = []
horses = []

for i in range(test_cases):
    cases.append(list(input().split()))
    d = int(cases[i][0])
    n = int(cases[i][1])
    horse = []
    for j in range(n):
        horse.append(list(input().split()))

    horses.append(horse)

for i in range(test_cases):
    d = int(cases[i][0])
    n = int(cases[i][1])
    print("Case #" + str(i + 1) + ": " + speed(d, n, horses[i]))


