from sys import stdin

def solve(prob):
    N = int(prob.pop(0))
    pos = [1, 1]
    t = [0, 0]
    for i in range(N):
        col, push = ('OB'.index(prob[2*i]), int(prob[2*i+1]))
        dt = abs(pos[col] - push) + 1
        t[col] += dt
        if t[col] <= t[1-col]:
            t[col] = t[1-col] + 1
        pos[col] = push
    return max(t)

buf = []
for line in stdin:
    buf.insert(0, line)
T = int(buf.pop())
for i in range(1, T+1):
    print 'Case #' + str(i) + ':',
    print solve(buf.pop().strip().split())
