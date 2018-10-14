tn = int(input())

for t in range(1, tn + 1):
    a = input().split()
    a, k = list(a[0]), int(a[1])
    cnt = 0
    for i in range(len(a) - k + 1):
        if a[i] == '-':
            for j in range(k):
                if a[i + j] == '-':
                    a[i + j] = '+'
                else:
                    a[i + j] = '-'
            cnt += 1
    if a != ["+"] * len(a):
        cnt = "IMPOSSIBLE"
    print("Case #%d:" % t, cnt)
