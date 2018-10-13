from sys import stdin, stdout
t = input()
for i in range(1, t+1):
    d,n = map(float, stdin.readline().split())
    arr = []
    n=int(n)
    for i in range(n):
        k,s = map(float, stdin.readline().split())
        arr.append([(d-k)/s, k, s])
    arr.sort(reverse = True)
    x = d/arr[0][0]
    print 'Case #%d: %0.6f'%(i,x)
