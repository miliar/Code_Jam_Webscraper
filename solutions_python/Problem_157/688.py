#!/usr/bin/python3
import functools

t = int(input())

mul = {'11': '1', '1i': 'i', '1j': 'j', '1k': 'k',
       'i1': 'i', 'ii': '-', 'ij': 'k', 'ik': 'b',
       'j1': 'j', 'ji': 'c', 'jj': '-', 'jk': 'i',
       'k1': 'k', 'ki': 'j', 'kj': 'a', 'kk': '-'}
rev = {'1': '-', '-': '1', 'i': 'a', 'a': 'i',
       'j': 'b', 'b': 'j', 'k': 'c', 'c': 'k'}

orig = list(mul.keys())

for k in orig:
    mul[rev[k[0]] + k[1]] = rev[mul[k]]
    mul[k[0] + rev[k[1]]] = rev[mul[k]]
    mul[rev[k[0]] + rev[k[1]]] = mul[k]


def q(inp):
    return functools.reduce(lambda x, y: mul[x + y], inp, '1')


def test(letters):
    starts = []
    saved = ''
    for i in range(len(letters) - 1):
        saved = mul.get(saved + letters[i], saved + letters[i])
        if saved == 'i':
            starts.append(i + 1)

    if starts == []:
        return False

    ends = []
    saved = ''
    for j in reversed(range(min(starts), len(letters))):
        saved = mul.get(letters[j] + saved, letters[j] + saved)
        if saved == 'k':
            ends.append(j)

    if ends == []:
        return False

    for i in starts:
        saved, save_mark = '', i
        for j in ends:
            saved = q(saved + letters[save_mark:j])
            if saved == 'j':
                return True
            save_mark = j
            if i < j:
                break
    return False


for test_num in range(t):
    _, chunks = [int(n) for n in input().split()]
    letters = input()

    cond = test(letters * chunks)
    print('Case #{}: {}'.format(test_num + 1, 'YES' if cond else 'NO'))
