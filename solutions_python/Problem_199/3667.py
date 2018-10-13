t = int(input())
s = []
for i in range(1, t + 1):
    n, m = [str(i) for i in raw_input().split(" ")]
    s.append((n,int(m)))
for i in range(0, len(s)):
    panList = list(s[i][0])
    k = s[i][1]
    count = 0
    possible = True
    if (k > len(panList)):
        print('Case #' + str(i+1) + ': ' + 'IMPOSSIBLE')
        break
    for j in range(0,len(panList) - k + 1):
        if(panList[j] == '-'):
            panList[j] = '+'
            for x in range(j + 1, j + k):
                if (panList[x] == '-'):
                    panList[x] = '+'
                else:
                    panList[x] = '-'
            count += 1
    for j in range(len(panList) - k, len(panList)):
        if(panList[j] == '-'):
            possible = False
    if(possible):
        print('Case #' + str(i+1) + ': ' + str(count))
    else:
        print('Case #' + str(i+1) + ': ' + 'IMPOSSIBLE')
