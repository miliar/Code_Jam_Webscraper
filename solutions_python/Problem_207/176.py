import numpy as np

NOPE = 'IMPOSSIBLE'
def arange_colors(N, R, O, Y, G, B, V):
    assert N == R + O + Y + G + B + V

    if G > 0:
        if R > G:
            R -= G
        elif R == G and R+G == N:
            return 'RG'*R
        else:
            print('G')
            return NOPE
    if V > 0:
        if Y > V:
            Y -= V
        elif Y == V and Y+V == N:
            return 'YV'*Y
        else:
            print('V')
            return NOPE
    if O > 0:
        if B > O:
            B -= O
        elif B == O and B+O == N:
            return 'BO'*B
        else:
            print('O')
            return NOPE

    result = ''
    result_indices = []
    ryb = [[R, 0, 0], [Y, 0, 1], [B, 0, 2]]     # counter, is_init_color, color_idx
    t3 = max(ryb)
    result_indices = [t3[2]]
    ryb[t3[2]][0] -= 1
    ryb[t3[2]][1] = 1
    while ryb[0][0] + ryb[1][0] + ryb[2][0] > 0:
        t1, t2, t3 = sorted(ryb)
        if result_indices[-1] != t3[2]:
            result_indices += [t3[2]]
            ryb[t3[2]][0] -= 1
        else:
            result_indices += [t2[2]]
            ryb[t2[2]][0] -= 1

    result = ''.join(['RYB'[idx] for idx in result_indices])

    result = result.replace('R', 'RG'*G + 'R', 1)
    result = result.replace('Y', 'YV'*V + 'Y', 1)
    result = result.replace('B', 'BO'*O + 'B', 1)

    print(result, ryb)
    if any([t[0] != 0 for t in ryb]) or result[0] == result[-1]:
        return NOPE

    return result



if __name__=='__main__':
    PATH_IN = 'B-large.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline()
        print(line.strip())
        N, R, O, Y, G, B, V = [int(c) for c in line.split()]

        res = arange_colors(N, R, O, Y, G, B, V)

        print('Case #%i: %s' % (t+1, res))
        print()
        f_out.write('Case #%i: %s\n' % (t+1, res))