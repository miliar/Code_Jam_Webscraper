file = open("A_large.in")
out  = open("ans.txt", "w")

input = file.readline
print = out.write

##def com():

T = int(input())
for t in range(T):
    D, N = map(int, input().split(' '))
    red = [[int(k) for k in input().split(' ')] for i in range(N)]
    m = 0
    for r in red:
        m = max(m, (D-r[0])/r[1])
    ans = str(D/m)
    print("Case #{}: {}\n".format(t+1, ans))
