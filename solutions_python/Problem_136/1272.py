n = int(input())
for i in range(n):
    path = []
    summary = []
    c,f,x = map(float, input().split())
    count = 2
    path.append((c/2, x/2))
    summary.append(x/2)
    for j in range(100000):
        count += f
        path.append((path[-1][0] + c/count, x/count))
        summary.append(x/count + path[-2][0])
    print('Case #',i+1,':',' ',min(summary), sep ='')

    