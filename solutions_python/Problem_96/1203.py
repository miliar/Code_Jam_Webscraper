import sys

"""
FACTS:
### if score/3 >= p-(2/3), then doesn't have to be surprising
AND could contain the max result
### score >= p but not above, then could contain max result
AND is surprising
### scores of 0, 1, 29, and 30 can NOT be surprising
### no way to say that something is for sure surprising
knowing only the score
"""

"""
Note: Did not see on first submission that
NO TRIPLET OF SCORES CONTAINS SCORES THAT ARE MORE
THAN 2 APART so revise second FACT to:
### score >= p + (p-2) + (p-2) = 3p - 4 could contain
max result and IS suprising
"""

def maxBestResult(scores, numSurprise, bestResult):
    maxBest = 0
    potential = 0
    if bestResult == 0:
        lower1 = 0
        lower2 = 0
    elif bestResult == 1:
        lower1 = 1
        lower2 = 1
    else:
        lower1 = 3*bestResult-2
        lower2 = 3*bestResult-4
    for score in scores:
        if score >= lower1:
            # doesn't have to be a suprise
            # AND could have the given best result
            maxBest += 1
        elif potential < numSurprise and score >= lower2:
            # IS a suprise but could have the given best result
            maxBest += 1
            potential += 1
    # some of the high scores had to be potentials
    return maxBest

f = open('dancegoogler-large.txt', 'w')
numTests = int(sys.stdin.readline())
lines = sys.stdin.readlines()
for i in range(1,numTests+1):
    line = lines[i-1].split()
    surprises = int(line[1])
    p = int(line[2])
    scores = map(int, line[3:])
    maxBest = maxBestResult(scores, surprises, p)
    f.write('Case #' + str(i) + ': ' + str(maxBest) + '\n')
f.close()