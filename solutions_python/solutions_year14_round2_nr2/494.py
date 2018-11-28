import sys

path = "test.in" if len(sys.argv) == 1 else sys.argv[1]
file = open(path, "r")
T = int(file.readline())

for casenum in range(T):
    A, B, K = [int(z) for z in file.readline().split()]
    count = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                count += 1
    print("Case #{0}: {1}".format(casenum+1, count))
