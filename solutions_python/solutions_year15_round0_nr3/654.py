import sys

I = 1
J = 2
K = 3
A = 4 # 1
_I = 5
_J = 6
_K = 7
_A = 8 #-1

d = {
    _A: {A: _A, I: _I, J: _J, K: _K},
    _I: {A: _I, I: A, J: _K, K: J},
    _J: {A: _J, I: K, J: A, K: _I},
    _K: {A: _K, I: _J, J: I, K: A},

    A: {A: A, I: I, J: J, K: K},
    I: {A: I, I: _A, J: K, K: _J},
    J: {A: J, I: _K, J: _A, K: I},
    K: {A: K, I: J, J: _I, K: _A},
}

t = {'i': I, 'j': J, 'k': K}


class Solved(Exception):
    pass


def calc(str):
    global d

    r = str[0]
    for i in str[1:]:
        r = d[r][i]

    return r


def load(str):
    global t

    r = []
    for i in str:
        r.append(t[i])

    return r

def solve(amount, data):
    global d

    r = None
    LF = [I, J, K]
    now = 0

    for _, i in enumerate(data):
        if r is None:
            r = i
        else:
            r = d[r][i]

        if now < 2 and r == LF[now]:
            now += 1
            r = None

    if now == 2 and r == K:
        raise Solved('YES')

    raise Solved('NO')


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        _, amount = map(int, sys.stdin.readline().strip().split(' '))
        s = sys.stdin.readline().strip() * amount

        try:
            solve(amount, load(s))
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
