import numpy as np

from sys import stdin

def printAnswer(caseIndex, answer):
	print("Case #", caseIndex+1, ": ", answer, sep='')

T = int(input())
for t in range(T):
    _, audience = input().split()
    shyness = list(map(int, (l for l in audience)))
    cum = np.cumsum(shyness)

    nb_added = 0
    for i, s in enumerate(cum):
        needed = (i + 1) - (s + nb_added)
        if needed > 0:
            nb_added += needed
    printAnswer(t, nb_added)
