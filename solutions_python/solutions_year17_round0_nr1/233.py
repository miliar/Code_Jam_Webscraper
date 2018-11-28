# coding: utf8

import sys


def flip_char(character):
    if character == '+':
        return '-'
    elif character == '-':
        return '+'
    else:
        raise ValueError(character)


def flip(string):
    return ''.join(flip_char(x) for x in string)


def main():
    T = int(sys.stdin.readline())
    for _T in range(T):
        S, K = sys.stdin.readline().split()
        K = int(K)
        flips = 0
        for i in range(len(S) - K + 1):
            if S[i] == '+':
                pass
            else:
                flips += 1
                S = S[:i] + flip(S[i:i + K]) + S[i + K:]
        if all(x == '+' for x in S):
            result = flips
        else:
            result = 'IMPOSSIBLE'
        print('Case #%s: %s' % (_T + 1, result))


if __name__ == '__main__':
    main()
