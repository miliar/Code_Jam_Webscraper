#!/usr/bin/env python3

def process(r1, g1, r2, g2):
    possibly = g1[r1]
    answers = [item for item in g2[r2] if item in possibly]
    if not answers:
        return 'Volunteer cheated!'
    elif len(answers) > 1:
        return 'Bad magician!'
    else:
        return answers[0]

if __name__ == '__main__':
    for i in range(int(input())):
        r1 = int(input()) - 1
        g1 = [input().split() for _ in range(4)]
        r2 = int(input()) - 1
        g2 = [input().split() for _ in range(4)]
        print('Case #{}: {}'.format(1+i, process(r1, g1, r2, g2)))
