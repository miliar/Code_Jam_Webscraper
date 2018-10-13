in_file = 'B-large.in'
out_file = 'B-large.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    n_digs = list(inp.readline().strip())
    l = len(n_digs)
    i = 0
    while i < l-1:
        if n_digs[i]*(l - i - 1) > ''.join(n_digs[i+1:]):
            n_digs[i] = str(int(n_digs[i]) - 1)
            for j in range(i+1, l):
                n_digs[j] = '9'
            break
        i += 1
    ans = int(''.join(n_digs))
    out.write('Case #{}: {}\n'.format(case, ans))

inp.close()
out.close()
