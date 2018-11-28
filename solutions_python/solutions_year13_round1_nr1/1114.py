def rings(r, t):
    t0 = t
    r2 = 2*r
    from math import floor
    i1 = floor((t/2)**(1/2))
    i2 = t//(r2)
    i = max(1, min(i1,i2))
    t -= i*(r2+2*i-1)
    if t < 0:
        while t < 0:
            t += r2 + 4*i + 1
            i -= 1
    elif t > 0:
        while t >= 0:
            t -= r2 + 4*i + 1
            i += 1
        i -= 1
        t += r2 + 4*i + 1
    return i

def main():
    name = input()
    lines = open(name+'.in').readlines()
    T = int(lines[0])
    s = ''
    for line in range(1,T+1):
        case = 'Case #'+str(line)+': '
        r,t = map(int, lines[line].split())
        #case += str(rings(r,t))
        paint = 0
        i = 0
        while paint <= t:
            paint += 2*r + 4*i + 1
            i += 1
        case += str(i-1)
        s += case + '\n'
    open(name+'.out', 'w').write(s)

if __name__ == '__main__':
    main()
