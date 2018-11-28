import re

def solve(cake):
    cake = [fill_row(row) for row in cake]
    prev = -1
    for i, row in enumerate(cake):
        if row[0] != '?':
            for j in range(prev+1, i):
                cake[j] = row
            prev = i
    if row[0] == '?':
        for j in range(prev+1, len(cake)):
            cake[j] = cake[prev]
    return cake


def fill_row(row):
    row = re.sub(r'\?+([^?])', lambda m: m.group().replace('?', m.group(1)), row)
    row = re.sub(r'([^?])\?+', lambda m: m.group().replace('?', m.group(1)), row)
    return row


def test_fill_row():
    assert fill_row('????') == '????'
    assert fill_row('???A') == 'AAAA'
    assert fill_row('?A?B') == 'AABB'
    assert fill_row('?A??') == 'AAAA'
    assert fill_row('BA??') == 'BAAA'


def test_solve():
    assert solve(['????', '?A??', '????']) == ['AAAA', 'AAAA', 'AAAA']
    assert solve(['?B??', '?A??', '????']) == ['BBBB', 'AAAA', 'AAAA']
    assert solve(['?B??', '?A??', '???C']) == ['BBBB', 'AAAA', 'CCCC']
    assert solve(['????', '?A??', '???C']) == ['AAAA', 'AAAA', 'CCCC']
    assert solve(['????', '?A??', '????'] * 10) == ['AAAA', 'AAAA', 'AAAA'] * 10


def main():
    T = int(input())
    for i in range(1, T+1):
        R, C = map(int, input().split())
        cake = [input() for j in range(R)]
        cake = solve(cake)
        print('Case #{}:'.format(i))
        for row in cake:
            print(row)

if __name__ == '__main__':
    main()
