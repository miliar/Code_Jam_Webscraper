# B.py

import sys
import os

def main():
    s = ''.join(sys.stdin.readlines()).split()
    os.close(0)

    T = int(s[0])
    s = s[1:]

    for i in range(T):
        C = int(s[0])
        s = s[1:]
        combinations = {}
        for j in range(C):
            combinations[(s[j][0],s[j][1])] = s[j][2]
            combinations[(s[j][1],s[j][0])] = s[j][2]
        s = s[C:]
        D = int(s[0])
        s = s[1:]
        oppositions = {}
        for j in range(D):
            try:
                oppositions[s[j][0]] += [s[j][1]]
            except KeyError:
                oppositions[s[j][0]] = [s[j][1]]
            try:
                oppositions[s[j][1]] += [s[j][0]]
            except KeyError:
                oppositions[s[j][1]] = [s[j][0]]
        s = s[D:]
        N = int(s[0])
        inseries = s[1]
        s = s[2:]
        outseries = []
        for j in inseries:
            if len(outseries) > 0 and (outseries[-1], j) in combinations:
                outseries[-1] = combinations[(outseries[-1], j)]
            elif oppositions.has_key(j) and any(k in outseries for k in oppositions[j]):
                outseries = []
            else:
                outseries += [j]
        print "Case #" + str(i + 1) + ": [" + ", ".join(outseries) + "]"

if __name__ == "__main__":
 	main()
