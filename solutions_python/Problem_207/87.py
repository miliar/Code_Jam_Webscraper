import argparse
import math

parser = argparse.ArgumentParser(description='Google Code Jam 2017')
parser.add_argument('fin')
parser.add_argument('fout')

args = parser.parse_args()

fin = args.fin
fout = args.fout


def solver(N, R, O, Y, G, B, V):
    t = math.floor(N / 2)
    ret = [''] * N
    Z = [R, O, Y, G, B, V]

    C = ['R', 'O', 'Y', 'G', 'B', 'V']
    if (R > t or Y > t or B > t
        or R + O > t or R + V > t
        or Y + O > t or Y + G > t
        or B + V > t or B + G > t):
        return 'IMPOSSIBLE'
    else:
        m = R
        z_ptr = 0
        for i in range(len(Z)):
            if Z[i] > m:
                m = Z[i]
                z_ptr = i
        if (N % 2 == 0):
            for i in range(N // 2):
                while Z[z_ptr % 6] <= 0:
                    z_ptr += 1
                ret[i * 2] = C[z_ptr % 6]
                Z[z_ptr % 6] -= 1

            for i in range(N // 2):
                while Z[z_ptr % 6] <= 0:
                    z_ptr += 1
                ret[i * 2 + 1] = C[z_ptr % 6]
                Z[z_ptr % 6] -= 1


        else:  # N%2 == 1
            for i in range(N):
                while Z[z_ptr % 6] <= 0:
                    z_ptr += 1
                ret[i * 2 % N] = C[z_ptr % 6]
                Z[z_ptr % 6] -= 1
    for i in range(len(ret)-1):
        if ret[i] == ret[i+1]:
            print(ret)
    if (ret[0] == ret[-1]):
        print(ret)
    return ''.join(ret)


with open(fin, 'r') as input, open(fout, 'w') as output:
    T = int(input.readline().rstrip('\n'))
    for i in range(0, T):
        s = input.readline().rstrip('\n')
        l = s.split(' ')
        N = int(l[0])  # N, R, O, Y, G, B, and V.
        R = int(l[1])
        O = int(l[2])
        Y = int(l[3])
        G = int(l[4])
        B = int(l[5])
        V = int(l[6])
        answer = 'Case #{}: {}\n'.format(i + 1, solver(N, R, O, Y, G, B, V))
        #print(answer)
        output.write(answer)
