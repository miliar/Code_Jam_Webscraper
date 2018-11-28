import sys, itertools
from collections import defaultdict
from copy import deepcopy
from pprint import pprint

phrase = "welcome to code jam"
letter_to_indexes = defaultdict(list)
for i, c in zip(itertools.count(), phrase):
    letter_to_indexes[c].append(i)
#pprint(letter_to_indexes)

def countsubstr(s):
    cur = defaultdict(lambda :0) #index->count
    cur[-1] = 1
    for c in s:
        last, cur = cur, deepcopy(cur)
        for i in letter_to_indexes[c]:
            #print(c,i,last[i-1])
            if last[i-1]:
                cur[i] = (cur[i] + last[i-1]) %10000
    return cur[len(phrase)-1]

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w') as outfile:
        N = int(infile.readline())
        for n in range(N):
            count = countsubstr(infile.readline())
            print("Case #{0:d}: {1:04d}".format(n+1, count), file=outfile)
            #print()
