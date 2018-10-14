f = open('B-large.in')
g = open('B-large-output.in', 'w')
T = int(f.readline())
x = 1
while T > 0:
    y = 0
    line = f.readline().split()
    N = int(line.pop(0))
    S = int(line.pop(0))
    p = int(line.pop(0))
    for i in line:
        score = int(i)
        if score % 3 == 0:
            if score // 3 >= p:
                y += 1
            elif S > 0 and score // 3 + 1 == p and score // 3:
                y += 1
                S -= 1
        else:
            if score // 3 + 1 >= p:
                y += 1
            elif S > 0 and score % 3 == 2 and score // 3 + 2 >= p:
                y += 1
                S -= 1
    if x != 1:
        g.write('\n')
    g.write('Case #{}: {}'.format(x, y))
    T -= 1
    x += 1
f.close()
g.close()
