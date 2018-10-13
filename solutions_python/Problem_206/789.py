import sys
input = open(sys.argv[1])


def solve(D, N):
    M = 0
    for _ in range(N):
        k, s = input.readline().split()
        M = max(M, (D - int(k)) / int(s))
    return D / M


for case in range(int(input.readline())):
    s, k = input.readline().split()
    print ("Case #%d: %.6f" % (case + 1, solve(int(s), int(k))))
