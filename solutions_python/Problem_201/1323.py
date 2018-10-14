import sys
from typing import Tuple
import math
import queue

class Room:
    def __init__(self, idx, num):
        self.idx = idx
        self.num = num

        self.min = math.ceil(num / 2) - 1
        if num % 2 == 0:
            self.max = self.min + 1
        else:
            self.max = self.min

    def __lt__(self, other: 'Room'):
        if self.min < other.min:
            return False
        elif self.min > other.min:
            return True

        if self.max < other.max:
            return False
        elif self.max > other.max:
            return True

        if self.idx < other.idx:
            return True
        elif self.idx > other.idx:
            return False

    def split(self):
        return [
            Room(self.idx, self.min),
            Room(self.idx+self.min + 1, self.max),
        ]

    def __repr__(self):
        return f'<R i={self.idx} n={self.num}>'


class Problem:
    def __init__(self, num, persons):
        self.num = num
        self.persons = persons
        self.data = queue.PriorityQueue()
        self.data.put(Room(0, num))

    def solve(self):
        for i in range(self.persons-1):
            r = self.data.get()
            for e in r.split():
                self.data.put(e)
        r = self.data.get()
        return r.max, r.min


def solve(prob) -> str:
    result = prob.solve()
    return ' '.join(map(str, result))

def parse(prob:str):
    n, p = map(int, prob.split(' '))
    return {'prob': Problem(n, p)}

def main():
    filename = sys.argv[1]
    with open(filename) as fp:
        num_prob, *data = fp.readlines()
        for idx, prob in enumerate(map(parse, data), start=1):
            result = solve(**prob)
            print(f'Case #{idx}: {result}')

if __name__ == '__main__':
    main()
