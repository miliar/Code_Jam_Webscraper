
from collections import namedtuple
from math import pi

Pancake = namedtuple('Pancacke', ['radius', 'height'])

def top(pcake):
    return pi * pcake.radius ** 2

def side(pcake):
    return pi * pcake.radius * 2 * pcake.height

def solve(data):
    k = data['k']
    pancakes = sorted(data['pancakes'])
    guess = [pancakes[i] for i in range(k)]
    area = sum(side(pcake) for pcake in guess) + top(guess[-1])
    for j in range(k, len(pancakes)):
        max_area = -1
        removal = -1
        for i, pcake in enumerate(guess):
            new_area = area - top(guess[-1]) + top(pancakes[j]) + side(pancakes[j]) - side(pcake)
            if new_area > max_area:
                max_area = new_area
                removal = i
        if max_area > area:
            del guess[removal]
            guess.append(pancakes[j])
            area = max_area
    return area


def read_input_data():
    n, k = (int(i) for i in input().split())
    pancakes = [Pancake(*(int(i) for i in input().split())) for _ in range(n)]
    return {'k': k, 'pancakes': pancakes}

def main():
    case_count = int(input())
    for case_no in range(1, case_count+1):
        print('Case #{0}: {1:.10f}'.format(case_no, solve(read_input_data())))

if __name__ == '__main__':
    main()
