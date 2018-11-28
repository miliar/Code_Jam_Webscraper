F = open('input.in')
o = open('out.txt', 'w')
n = int(F.readline())
for q in range(n):
    c,f,x = map(float, F.readline().split())
    d = c/2
    t = 0
    y = 0
    inc = 2
    o.write("Case #{}: ".format(q+1))
    best = -1
    while True:
        remain = t + x/inc
        if best == -1 or remain < best: 
            best = remain
        else:
            o.write(str(best) + '\n')
            break
        t+=d
        inc += f
        d = c/inc

