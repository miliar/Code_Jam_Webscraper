import sys

def d(*args):
    sys.stderr.write(', '.join(map(str, args)) + "\n")

def printf(*args):
    print(''.join(map(str, args)))

def int_input():
    return list(map(int, input().split(' ')))

def solve(n, s):
    nb = s[0]
    toadd = 0
    for i in range(1, n+1):
        if nb < i:
            toadd += (i-nb)
            nb = i
        nb += s[i]
    return toadd

def read_input():
    s = input().split(' ')
    return int(s[0]), list(map(int, s[1]))


if __name__ == '__main__':
    for i in range(int(input())):
        printf("Case #", i+1, ": ", str(solve(*read_input())))
