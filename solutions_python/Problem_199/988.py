T = int(input())

for t in range(T):
    s, k = input().split()
    k = int(k)
    s = list(s)

    count = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            for x in range(i,i+k):
                s[x] = '+' if s[x] == '-' else '-'
            count += 1


    if '-' not in s:
        print("Case #%d: %d" % (t+1, count) )
    else:
        print("Case #%d: IMPOSSIBLE" % (t+1) )
