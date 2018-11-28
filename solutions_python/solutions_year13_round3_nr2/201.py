def f(a, b):
    for i in range(b):
        print('SN', end = '')
    for i in range(a):
        print('WE', end = '')
    for i in range(0, b, -1):
        print('NS', end = '')
    for i in range(0, a, -1):
        print('EW', end = '')
                

quant = int(input())
for qw in range(quant):
    print('Case #' + str(qw + 1) + ': ', end = '')
    a = input().split()
    f(int(a[0]), int(a[1]))
    print()
