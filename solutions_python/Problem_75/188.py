import sys
import re

def main():
    infile = open(sys.argv[1])
    T = int(infile.readline().strip())

    for i in range(0, T):
        C = {}
        D = {}
        N = []
        j = 0
        els = infile.readline().strip().split()
        for j in range(1, int(els[0])+1):
            e1, e2, r = list(els[j])
            if e1 not in C:
                C[e1] = {}
            if e2 not in C:
                C[e2] = {}
            C[e1][e2] = r
            C[e2][e1] = r
        j += 1
        for j in range(j+1, j+int(els[j])+1):
            e1, e2 = list(els[j])
            if e1 not in D:
                D[e1] = {}
            if e2 not in D:
                D[e2] = {}
            D[e1][e2] = 1
            D[e2][e1] = 1
        j += 2
        N = list(els[j])

        result = [N[0]]
        for j in range(1, len(N)):
            if result and N[j] in C and result[-1] in C[N[j]]:
                last = result.pop()
                result.append(C[N[j]][last])
            else:
                result.append(N[j])

            if result[-1] in D:
                for k in range(0, len(result)-1):
                    if result[k] in D[result[-1]]:
                        result = []
                        break
        print "Case #" + str(i+1) + ": [" + ", ".join(result) + "]"

if __name__ == "__main__":
    main()
