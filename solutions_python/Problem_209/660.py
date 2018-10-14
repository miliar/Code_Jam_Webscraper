import sys
from itertools import combinations

from math import pi

def parseCase(fin):
    line = next(fin).strip()
    N, K = map(int, line.split(' '))
    pancakes = []
    for i in range(N):
        line = next(fin).strip()
        Ri, Hi = map(int, line.split(' '))
        pancakes.append( (Ri, Hi) )
    return K, pancakes



def solve(k, pancakes):
    pancakes.sort(key=lambda x: x[0], reverse=True)
    answer = 0

    for sublist in combinations(pancakes, k):
        square = sum(2*r*h for (r,h) in sublist)
        square += sublist[0][0]**2
        answer = max(square, answer)

    return answer*pi


def main(filenameIn, filenameOut):
    with open(filenameIn, 'rt') as fin, open(filenameOut, 'wt') as fout:
        line = next(fin).strip()
        count = int(line)
        for i in range(count):
            k, pancakes = parseCase(fin)
            answer = solve(k, pancakes)
            fout.write("Case #{}: {:0.8f}\n".format(i+1, answer))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
