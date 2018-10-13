# -*- coding: utf-8 -*-

import sys
import math


class Pancake(object):
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def side_area(self):
        return self.radius * 2 * self.height * math.pi

    def top_area(self):
        return self.radius ** 2 * math.pi

    def __str__(self):
        return str(self.radius) + ' ' + str(self.height) + ' ' + \
               str(self.side_area()) + ' ' + str(self.top_area())


def solve(pancakes, k):
    if k == 1:
        return max([
            p.side_area() + p.top_area() for p in pancakes
        ])
    pancakes.sort(key=lambda x: x.top_area(), reverse=True)
    pancakes.sort(key=lambda x: x.side_area(), reverse=True)
    answer_candidate = sum([p.side_area() for p in pancakes[:k]]) + \
        max([p.top_area() for p in pancakes[:k]])

    pancakes.sort(key=lambda x: x.top_area())
    pancakes.sort(key=lambda x: x.side_area(), reverse=True)
    tower = pancakes[:(k-1)]
    rest = pancakes[(k-1):]
    tower_base = max([p.radius for p in tower])
    base_candidate = [p for p in rest if p.radius >= tower_base]
    if len(base_candidate) == 0:
        return answer_candidate
    else:
        base_candidate.sort(key=lambda x: x.side_area() + x.top_area(),
                            reverse=True)
        base = base_candidate[0]
        tower.append(base)
        answer2 = sum([p.side_area() for p in tower]) + max([p.top_area() for p in tower])
    if answer2 > answer_candidate:
        return answer2
    else:
        return answer_candidate


if __name__ == '__main__':
    problems = int(sys.stdin.readline())
    for i in range(1, problems + 1):
        header = sys.stdin.readline().strip().split(' ')
        n = int(header[0])
        k = int(header[1])
        pancakes = []
        for j in range(n):
            ln = sys.stdin.readline().strip().split(' ')
            pancakes.append(Pancake(float(ln[0]), float(ln[1])))
        sys.stdout.write('Case #{}: {}\n'.format(i, solve(pancakes, k)))
