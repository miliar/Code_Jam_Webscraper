def solve(num):
    print("Case #" + str(num) + ": ", end = "")
    C, F, X = map(float, input().split())
    ans = X / 2.0
    speed = 2.0
    time = 0
    while time < ans:
        ans = min(ans, time + X / speed)
        time += C / speed
        speed += F
    print(ans)

T = int(input())
for i in range(T):
    solve(i + 1)


