# coding: utf-8
import sys
from itertools import groupby

def testcases():
    with open(sys.argv[1], "r") as f:
        T = int(f.readline())
        for X in range(1, T + 1):
            tmp = [ int(v) for v in f.readline().split() ]
            yield X, tmp[0], tmp[1:]

def main():
    for X, N, S in testcases():

        print("Case #{}:".format(X))

        ccc = {}
        for n in range(1, pow(2, 20) + 1):
            cc = format(n, '020b')
            s = 0
            ss = []
            for i in range(N):
                if cc[i] == '1':
                    s += S[i]
                    ss.append(str(S[i]))
            if s in ccc:
                print(" ".join(ss))
                print(" ".join(ccc[s]))
                break
            else:
                ccc[s] = ss
        else:
            print("Impossible")

if __name__=="__main__":
    main()
