import sys
import glob


def findTidy(n):
    # while True:
    #     nu = [int(i) for i in list(str(n))]
    #     limit = nu[0]
    #
    #     for i in range(0, len(nu)):
    #         if nu[i] < limit: break
    #         if i is len(nu) - 1: return str(n)
    #         if nu[i] > limit: limit = nu[i]
    #
    #     n -= 1

    while True:
        limit, limit_index = n[0], 0
        for i in range(0, len(n)):
            if n[i] < limit:
                temp = ''.join("9" * len(n[limit_index:-1]))
                n = ''.join(str(int(n[:limit_index] + str(int(limit) - 1) + temp)))
                break

            if i + 1 == len(n): return n

            if n[i] > limit:
                limit = n[i]
                limit_index = i

inputFiles = []
if len(sys.argv) == 2 and str(sys.argv[1]) == "-l": inputFiles = glob.glob('*-large*.in')
elif len(sys.argv) == 2 and str(sys.argv[1]) == "-s": inputFiles = glob.glob('*-small*.in')
else: inputFiles = glob.glob('sample.in')

for fn in inputFiles:
    with open(fn) as f:
        T = int(f.readline())
        lines = [line.strip() for line in f.readlines()]

        for x in range(0, T):
            print( "Case #" + str(x+1) + ": " + findTidy(lines[x]) )
