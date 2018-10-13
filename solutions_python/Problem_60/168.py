import sys, itertools
from pprint import pprint
from collections import namedtuple

output_line = "Case #{X:d}: {S:s}"

Chicken = namedtuple("Chicken", "velocity location time_required")

if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        C = int(inhandle.readline())
        for c in range(C):
            N, K, B, T = map(int, inhandle.readline().split())

            chick_X = map(int, inhandle.readline().split())
            chick_V = map(int, inhandle.readline().split())

            chicks = [Chicken(V, X, (B - X) / V) for X, V in zip(chick_X, chick_V)]
            chicks.reverse()
            print(chicks)

            swaps = 0


            finished_chicks = 0
            slow_chick_count = 0
            for i, chick in enumerate(chicks):
                if finished_chicks >= K:
                    break
                if chick.time_required <= T:
                    swaps += slow_chick_count
                    finished_chicks += 1
                else:
                    slow_chick_count += 1

            if finished_chicks < K:
                swaps = "IMPOSSIBLE"
            else:
                swaps = str(swaps)

            print(output_line.format(X=c + 1, S=swaps), file=outhandle)
