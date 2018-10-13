__author__ = 'mike'
import numpy as np


def solve(cipher):
    cipher = cipher.split(' ')
    max_expected = int(cipher[0])
    S = [int(i) for i in cipher[1]]
    total = 0
    for i, s in enumerate(S):
        if s == 0:
            continue
        if total >= i:
            total += s
        else:
            total += (i - total) + s
    solution = np.clip(int(total - np.sum(S)), 0, np.inf)
    return int(solution)


if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases + 1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))

