for t in range(int(input())):
    print("Case #%s: " % str(t + 1), end="")
    line = input().split()
    s = list(line[0])
    k = int(line[1])
    flips = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            flips += 1
            for j in range(k):
                idx = i + j
                if s[idx] == '-':
                    s[idx] = '+'
                else:
                    s[idx] = '-'
    if '-' in s:
        print("IMPOSSIBLE")
    else:
        print(flips)
