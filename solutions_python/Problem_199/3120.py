def flip(p, i, k):
    for j in range(i, i+k):
        p[j] = not p[j]

file = open('A-large.in', 'r') # r for read
out = open('a.out', 'w') # w for write
#
n = int(file.readline().strip()) 
for c in range(n):
    l = file.readline().strip().split(' ')
    p = [True if e == '+' else False for e in l[0]]
    k = int(l[1])
    m = 0
    for i in range(len(p)-k+1):
        if not p[i]:
            flip(p, i, k)
            m += 1
    out.write('Case #{}: '.format(1+c))
    if sum(p) != len(p):
        out.write('IMPOSSIBLE\n')
    else:
        out.write(str(m) + '\n')
#
file.close()
out.close()