T = int(input())
for t in range(1, T + 1):
    C, F, X = map(float, input().split())
    min = X / 2.0
    time = 0.0
    inc = 2.0
    while time <= min:
        time += C / inc
        inc += F
        if time + X / inc < min:
            min = time + X / inc
    print("Case #" + str(t) + ": " + str(min))