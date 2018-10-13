#! /usr/bin/env python


def main():
    with open('b.in', 'r') as fin, open('b.out', 'w') as fout:
        num_cases = int(fin.readline())
        for case in range(1, num_cases + 1):
            n = int(fin.readline())
            answer = solve(n)
            fout.write('Case #{0}: {1}\n'.format(case, answer))


def solve(n):
    # Find smallest i s.t. m[i] > m[i+1], tail = '9'* len(m[i+1:])
    # Then find biggest tidy number < m[:i+1] for the head
    m = list(map(int, str(n)))
    first_decrease_index = None

    for i, (v1, v2) in enumerate(zip(m, m[1:]), 1):
        if v1 > v2:
            first_decrease_index = i
            break
    else:
        return str(n)

    tail = '9' * len(m[first_decrease_index:])

    head = int(''.join(map(str, m[:first_decrease_index]))) - 1
    if list(str(head)) != list(sorted(str(head))):
        head = solve(head)

    if head:
        return str(head) + tail
    return tail


if __name__ == '__main__':
    main()
