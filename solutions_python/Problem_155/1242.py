case = open('file.txt')

t = int(case.readline().rstrip())

for c in range(t):
    smax, dist = case.readline().rstrip().split()
    curr = 0
    ans = 0
    for i in range(int(smax)+1):
        if int(dist[i]):
            while curr < i:
                ans += 1
                curr += 1
        curr += int(dist[i])
    print('Case #{}: {}'.format(c+1,ans))
case.close()
