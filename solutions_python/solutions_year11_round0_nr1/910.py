import sys

def solve_case(line, fout):
    parts = line.split()
    N = int(parts[0])
    buttons = tuple((parts[i], int(parts[i+1])) for i in range(1, len(parts)-1, 2))
    t, bx, ox = 0, 1, 1
    for i, button in enumerate(buttons):
        bot, x = button
        if bot == 'B':
            dt = abs(x - bx) + 1
            bx = x
            other, otherx = 'O', ox
        elif bot == 'O':
            dt = abs(x - ox) + 1
            ox = x
            other, otherx = 'B', bx
        nextother = [b for b in buttons[i+1:] if b[0] == other]
        if len(nextother) > 0:
            nextotherx = nextother[0][1]
            if abs(nextotherx - otherx) <= dt:
                otherx = nextotherx
            elif nextotherx > otherx:
                otherx += dt
            else:
                otherx -= dt
        if other == 'B':
            bx = otherx
        else:
            ox = otherx
        t += dt
    return str(t)



def test():
    inpath, outpath = 'test.in', 'test.out'
    line = fin.readline().strip()

def main(inpath, outpath):
    fin = open(inpath)
    T = int(fin.readline().strip())
    fout = open(outpath, 'w')
    for t in range(T):
        print >>fout, 'Case #%d: %s' % (t+1, solve_case(fin.readline().strip(), fout))
    fin.close()
    fout.close()


main(sys.argv[1], sys.argv[2])
