N = int(input())
for num in range(1, N + 1):
    inp = input()
    inp = list(map(int,input().split()))
    s = len(inp)
    for i in range(len(inp)):
        if inp[i] == i + 1:
            s -= 1
    print("Case #", num, ": ", s, sep = '')
