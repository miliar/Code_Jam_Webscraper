T = int(input())

for t in range(1, T+1):
    As, Bs = input().split()
    A = int(As)
    B = int(Bs)
    result = 0
    added = set()
    for i in range(A, B+1):
        added.clear()
        s = str(i)
        for j in range(1, len(s)):
            if s[-j] == '0':
                continue
            news = s[-j:] + s[:-j]
            newi = int(news)
            if newi not in added and newi > i and newi <= B:
                added.add(newi)
        result += len(added)
    print('Case #' + str(t) + ':', result)