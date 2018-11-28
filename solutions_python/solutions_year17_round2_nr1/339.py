in_file = 'A-large.in'
out_file = 'A-large.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    d, n = list(map(int, inp.readline().split()))
    max_time = 0
    for i in range(n):
        k, s = list(map(int, inp.readline().split()))
        time = (d-k)/s
        if time > max_time:
            max_time = time

    ans = d/max_time

    out.write('Case #{}: {}\n'.format(case, ans))

inp.close()
out.close()
