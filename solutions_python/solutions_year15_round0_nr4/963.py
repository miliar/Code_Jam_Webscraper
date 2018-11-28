#! /usr/bin/env python


def main():
    with open('d.in', 'r') as fin, open('d.out', 'w') as fout:
        num_cases = int(fin.readline())
        for case in range(1, num_cases + 1):
            x, r, c = map(int, fin.readline().split())
            answer = solve(x, r, c)
            fout.write('Case #{0}: {1}\n'.format(case, answer))
    return


def solve(x, r, c):
    # is Gabriel guaranteed to win (no matter what Richard chooses)
    yes = "GABRIEL"
    no = "RICHARD"

    if x == 1:
        return yes
    elif x == 2:
        if r*c %2 or r*c == 1:
            return no
        return yes
    elif x == 3:
        if (r, c) in [(2,3), (3,2), (3,3), (3,4), (4,3)]:
            return yes
        return no

    elif x == 4:
        if (r, c) in [(4,3), (3, 4), (4, 4)]:
            return yes
        return no


if __name__ == '__main__':
    main()
