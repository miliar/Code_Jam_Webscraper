def solve(num, inp, out):
    res_t = 0
    D, N = map(int, inp.readline().split())
    for j in range(N):
        K, S = map(int, inp.readline().split())
        T = ((D - K)*1.0) / S
        res_t = max(T, res_t)
    try:
        out.write("Case #{}: {}\n".format(num+1, round(D / res_t, 6)))
    except:
        print(num)



inp = open('in.txt', 'r')
out = open('out.txt', 'w')
t = int(inp.readline())
for i in range(t):
    solve(i, inp, out)