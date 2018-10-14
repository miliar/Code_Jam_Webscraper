import sys

FILENAME = sys.argv[1]
# FILENAME = "sample_input.txt"

file = open(FILENAME)

T = int(file.readline().strip())

for i in range(T):
    D,N = map(int, file.readline().strip().split())
    ans = float("inf")
    for j in range(N):
        K,S = map(int, file.readline().strip().split())
        ans = min(ans, (D*S*1.0)/(D-K))

    print "Case #" + str(i + 1) + ": " + "{0:.6f}".format(ans)
