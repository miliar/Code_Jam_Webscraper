test = int(input())
for it in range(1,test+1):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    first = 0
    rate = 0
    for i in range(len(a)-1):
        rate = max(a[i]-a[i+1],rate)
        if a[i+1]>a[i]:
            continue
        else:
            first += a[i]-a[i+1]
    second = 0
    for i in range(len(a)-1):
        second += min(rate,a[i])
    print('Case #{}: {} {}'.format(it,first,second))#rate*(len(a)-1)))
