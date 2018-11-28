with open('C-large.in', 'r') as f:
    lines = f.readlines()
T = int(lines[0].strip())
lines = lines[1:T+1]

# 1001 -> 500, 500
# 1000 -> 500, 499
def solve(N, K):
    if K == 1:
        return N/2, N-1-N/2
    if N & 1:
        return solve(N/2, K/2)
    else:
        return solve(N/2-(K&1), K/2)


g = open('C_large_output.txt', 'w')

for t, line in enumerate(lines):
    N, K = line.strip().split(' ')
    N = int(N)
    K = int(K)
    a, b = solve(N, K)
    # print('Case #%d: %s %s' % (t+1, str(a), str(b)))
    g.write('Case #%d: %s %s' % (t+1, str(a), str(b)) + '\n')

g.close()
