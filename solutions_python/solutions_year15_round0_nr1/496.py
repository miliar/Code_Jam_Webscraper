for t in range(1, int(input()) + 1):
    inp = input().split()[1]
    cNumber = 0
    answer = 0
    for s, num in enumerate(map(int, inp)):
        if cNumber < s:
            answer += s - cNumber
            cNumber = s
        cNumber += num
    print("Case #{}: {}".format(t, answer))
