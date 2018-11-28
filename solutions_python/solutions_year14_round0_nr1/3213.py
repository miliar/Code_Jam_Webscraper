import sys, itertools
from collections import namedtuple
from itertools import chain, cycle
from pprint import pprint

output_line = "Case #{X:d}: {answer}"


if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            row1 = int(inhandle.readline())
            cards1 = [list(map(int, inhandle.readline().split())) for row in range(4)]
            row2 = int(inhandle.readline())
            cards2 = [list(map(int, inhandle.readline().split())) for row in range(4)]

            possible = set(cards1[row1 - 1]) & set(cards2[row2 - 1])

            if not possible:
                answer = "Volunteer cheated!"
            elif len(possible) > 1:
                answer = "Bad magician!"
            else:
                answer = possible.pop()

            outline = output_line.format(X=t + 1, answer=answer)
            print(outline, file=outhandle)
            print(outline)
