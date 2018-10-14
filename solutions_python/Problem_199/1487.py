t = int(input())
for i in range(t):
    line = input().split()
    s, k = line[0], int(line[1])
    arr = [False] * len(s)
    for j in range(len(s)):
        if s[j] == '+':
            arr[j] = True
    moves = 0
    for j in range(len(s) - k + 1):
        if not arr[j]:
            moves += 1
            for x in range(k):
                arr[j + x] = not arr[j + x]
    if any(not c for c in arr):
        print('Case #%d: IMPOSSIBLE' % (i + 1))
    else:
        print('Case #%d: %d' % (i + 1, moves))
