n = int(input())
for i in range(n):
    line = input().split()
    k = int(line[1])
    s = []
    for j in range(len(line[0])):
        s.append(line[0][j] == '+')

    count = 0
    for j in range(len(s)-k+1):
        if not(s[j]):
            for l in range(k):
                s[j+l] ^= True
            count += 1
    print("Case #{}: ".format(i+1), end="" )
    if not(all([s[-j] for j in range(k)])):
        print("IMPOSSIBLE")
    else:
        print(count)
