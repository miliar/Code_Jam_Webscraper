#! /usr/bin/env python

def main():
    with open('a.in', 'r') as fin, open('a.out', 'w') as fout:
        num_cases = int(fin.readline())
        for case in range(1, num_cases + 1):
            matched_rows = []
            for _ in range(2):
                rownum = int(fin.readline()) - 1
                match = [fin.readline().split() for row in range(4)][rownum]
                matched_rows.append(set(match))
            answer = solve(matched_rows)
            fout.write('Case #{0}: {1}\n'.format(case, answer))
    return

def solve(matched_rows):
    answer = matched_rows[0].intersection(matched_rows[1])
    if len(answer) == 0:
        return 'Volunteer cheated!'
    elif len(answer) == 1:
        return answer.pop()
    else:
        return 'Bad magician!'


if __name__ == '__main__':
    main()
