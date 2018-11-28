import itertools

def solve(r, y, b):
    if max(r,y,b) > (r+y+b)/2 or min(r,y,b)<0:
        return None
    ans = []
    filly, fillr = 0, 0
    if max(r, y, b) == r:
        ans = ['R', 'B' , ''] * b + ['R', 'Y', ''] * (r-b)
        filly = y-(r-b)
    elif max(r, y, b) == y:
        ans = ['Y', 'B', ''] * b + ['Y', 'R', ''] * (y-b)
        fillr = r-(y-b)
    else:
        ans = ['B', 'Y', ''] * y + ['B', 'R', ''] * (b-y)
        fillr = r-(b-y)
    if filly:
        for x in range(len(ans)):
            if ans[x] == '' and ans[x-1] != 'Y':
                if filly == 0:
                    break
                filly -= 1
                ans[x] = 'Y'
    else:
        for x in range(len(ans)):
            if fillr == 0:
                break
            if ans[x] == '' and ans[x-1] != 'R':
                fillr -= 1
                ans[x] = 'R'
    return ''.join(ans)

if __name__ == '__main__':
    filein = open('B-small-attempt2.in', 'r')
    fileout = open('B-small-attempt2.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t + 1))
        [N, R, O, Y, G, B, V] = map(int, filein.readline().split())

        Rt, Yt, Bt = R - G, Y - V, B - O
        ans = solve(Rt, Yt, Bt)
        if ans is None:
            ans = 'IMPOSSIBLE'
        else:
            l = list(ans)
            temp = []
            if G != 0:
                temp.append(('R', 'R' + 'GR' * G))
            if V != 0:
                temp.append(('Y', 'Y' + 'YV' * V))
            if O != 0:
                temp.append(('B', 'B' + 'BO' * O))
            for _, a in temp:
                try:
                    i = next(i for i, x in enumerate(l) if x == 'R')
                    l[i] = a
                except StopIteration:
                    l.append(a[1:])
            ans = ''.join(l)
        fileout.write(ans + '\n')

    filein.close()
    fileout.close()