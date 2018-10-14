N = int(input())

for num in range(1, N + 1):
    inp = input()
    inp = list(map(int,input().split()))
    s = 0
    for elem in inp:
        s ^= elem
    if s == 0:
        m = min(inp)
        s = sum(inp)
        ans = s - m
        print("Case #", num, ": ", ans, sep = '')
    else:
        print("Case #", num, ": NO", sep = '')
