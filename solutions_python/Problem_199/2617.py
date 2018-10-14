t = int(raw_input())

for i in range(t):
    pancakes, k = map(str, raw_input().split())
    pancakes = list(pancakes)
    k = int(k)
    flips = 0
    for j in range(len(pancakes)-k+1):
        if pancakes[j]=='-':
            flips+=1
            for l in range(j, j+k):
                if pancakes[l]=='-':
                    pancakes[l] = '+'
                else:
                    pancakes[l] = '-'
    if '-' in pancakes:
        for j in range(len(pancakes)-1,len(pancakes)-k,-1):
            if j<k:
                break
            else:
                if pancakes[j]=='-':
                    flips+=1
                    for l in range(j, j-k, -1):
                        if pancakes[l]=='-':
                            pancakes[l] = '+'
                        else:
                            pancakes[l] = '-'
    if '-' in pancakes:
        print 'Case #{}: IMPOSSIBLE'.format(i+1)
    else:
        print "Case #{}: {}".format(i+1,flips)
