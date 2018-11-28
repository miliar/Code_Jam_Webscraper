import sys


def read():
    return sys.stdin.readline().strip()

def solve(s_max, S):
    standing = 0
    friends = 0
    for i in range(s_max + 1):
        if standing < i:
            d = i - standing
            friends += d
            standing += d + int(S[i])
        else:
            standing += int(S[i])

    return friends

numcases = int(sys.stdin.readline().strip())

for i in range(numcases):
    l = read().split()
    s_max, S = int(l[0]), l[1]
    print("Case #" + str(i+1) + ": " +
          str(solve(s_max, S)))
