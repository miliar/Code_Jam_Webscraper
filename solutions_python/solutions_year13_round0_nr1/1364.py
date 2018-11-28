def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        b = []
        b.append(in_stream.readline())
        b.append(in_stream.readline())
        b.append(in_stream.readline())
        b.append(in_stream.readline())
        in_stream.readline()
        if check_win(b, 'O'):
            out_stream.write('Case #%d: O won\n' % (tc + 1))
        elif check_win(b, 'X'):
            out_stream.write('Case #%d: X won\n' % (tc + 1))
        elif check_draw(b):
            out_stream.write('Case #%d: Draw\n' % (tc + 1))
        else:
            out_stream.write('Case #%d: Game has not completed\n' % (tc + 1))

def check_win(b, mark):
    d1, d2 = True, True
    for i in range(4):
        if b[i][i] != mark and b[i][i] != 'T':
            d1 = False
        if b[i][3 - i] != mark and b[i][3 - i] != 'T':
            d2 = False
        h, v = True, True
        for j in range(4):
            if b[i][j] != mark and b[i][j] != 'T':
                h = False
            if b[j][i] != mark and b[j][i] != 'T':
                v = False
        if h or v:
            return True
    return d1 or d2

def check_draw(b):
    for i in range(4):
        for j in range(4):
            if b[i][j] == '.':
                return False
    return True

if __name__ == '__main__':
#     import sys
#     main(sys.stdin, sys.stdout)
     main(open("A-large.in", "r"), open("a-large.out.txt", "w"))
