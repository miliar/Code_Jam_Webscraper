import sys


def solve(pie):
    pie = [list(l.strip()) for l in pie]

    chars = {}  # top left, bot right

    for y, l in enumerate(pie):
        for x, c in enumerate(l):
            if c != '?':
                if c not in chars:
                    chars[c] = (x, y, x, y)
                else:
                    tlx, tly, brx, bry = chars[c]
                    tlx = min(tlx, x)
                    tly = min(tly, y)
                    brx = max(brx, x)
                    bry = max(bry, y)
                    chars[c] = tlx, tly, brx, bry
    for c, tlbr in chars.items():
        tlx, tly, brx, bry = tlbr
        for x in range(tlx, brx+1):
            for y in range(tly, bry+1):
                print(y, x, file=sys.stderr)
                if pie[y][x] != '?' and pie[y][x] != c:
                    print("WTF OMG SHIT", x, y, file=sys.stderr)
                else:
                    pie[y][x] = c
    for c, tlbr in chars.items():
        tlx, tly, brx, bry = tlbr
        while tlx > 0:
            ok = False
            for x in range(tlx-1, brx+1):
                bad = False
                for y in range(tly, bry+1):
                    if pie[y][x] != '?' and pie[y][x] != c:
                        bad = True
                        break
                if bad:
                    break
            else:
                tlx -= 1
                ok = True
            if not ok:
                break
        while tly > 0:
            ok = False
            for x in range(tlx, brx+1):
                bad = False
                for y in range(tly-1, bry+1):
                    if pie[y][x] != '?' and pie[y][x] != c:
                        bad = True
                        break
                if bad:
                    break
            else:
                tly -= 1
                ok = True
            if not ok:
                break
        while brx < len(pie[0])-1:
            ok = False
            for x in range(tlx, brx+2):
                bad = False
                for y in range(tly, bry+1):
                    if pie[y][x] != '?' and pie[y][x] != c:
                        bad = True
                        break
                if bad:
                    break
            else:
                brx += 1
                ok = True
            if not ok:
                break
        while bry < len(pie)-1:
            ok = False
            for x in range(tlx, brx+1):
                bad = False
                for y in range(tly, bry+2):
                    if pie[y][x] != '?' and pie[y][x] != c:
                        bad = True
                        break
                if bad:
                    break
            else:
                bry += 1
                ok = True
            if not ok:
                break
        for x in range(tlx, brx+1):
            for y in range(tly, bry+1):
                if pie[y][x] != '?' and pie[y][x] != c:
                    print("WTF OMG SHIT", x, y, file=sys.stderr)
                else:
                    pie[y][x] = c

    return "\n".join([""]+["".join(l) for l in pie])


def solve_inputs(inputs):
    cnt = int(inputs[0])
    inputs = inputs[1:]
    for i in range(cnt):
        y, x = map(int, inputs[0].split())
        print("Case #{}:{}".format(i + 1, solve(inputs[1:1+y])))
        inputs = inputs[1+y:]


def main():
    solve_inputs(sys.stdin.readlines())

if __name__ == '__main__':
    main()
