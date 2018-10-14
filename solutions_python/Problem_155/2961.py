#! /usr/bin/python3

from sys import stdin

def ticketToTheGala(S_max, S_i):
    C = 0
    up = S_i[0]

    for i in range(1, S_max+1):
        diff = i - up
        up += S_i[i]

        if diff > 0:
            C += diff
            up += diff

    return C


if __name__ == '__main__':

    T = int(stdin.readline())
    for i in range(T):

        in_line = stdin.readline().split()
        S_max = int(in_line[0])
        S_i = [ 0 for x in range(S_max+1) ]

        for j in range(S_max+1):
            S_i[j] = int(in_line[1][j])

        print('Case #{}: {}'.format(i+1, ticketToTheGala(S_max, S_i)))


