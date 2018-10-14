t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    l = [0, n+1]
    for x in range(k - 1):
        m = 0
        for j in range(len(l) - 1):
            if m < l[j + 1] - l[j]:
                m = l[j + 1] - l[j]
                index = j
        l.append((l[index + 1] + l[index]) // 2)
        l.sort()
    m = 0
    for j in range(len(l) - 1):
        if m < l[j + 1] - l[j]:
            m = l[j + 1] - l[j]
            index = j
    print("Case #{}: ".format(i+1),end="")
    print(max((l[index + 1] + l[index]) // 2 - l[index] - 1, l[index + 1] - (l[index + 1] + l[index]) // 2 - 1), end = " ")
    print(min((l[index + 1] + l[index]) // 2 - l[index] - 1, l[index + 1] - (l[index + 1] + l[index]) // 2 - 1))        
