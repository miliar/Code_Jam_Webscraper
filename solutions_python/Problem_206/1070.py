'''
Code Jam 2017
1 B
'''
T = int(input())
for i in range(1, T + 1):
    n, m = [int(s) for s in input().split(" ")]
    longest = 0    
    for j in range(0, m):
        p, v = [int(s) for s in input().split(" ")]
        t = (n - p) / v
        if t > longest:
            longest = t
    _v = n / longest
    print("Case #{}: ".format(i) + "{0:.6f}".format(_v))