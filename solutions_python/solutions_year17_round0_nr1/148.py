import sys

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

def flip(char):
    if char == '-':
        return '+'
    return '-'

for testCase in range(T):
    line = input().split()
    S = list(line[0])
    K = int(line[1])

    count = 0
    i = 0
    while i < len(S):
        if i + K > len(S):
            break
        if S[i] == '-':
            count += 1
            for j in range(i, i + K):
                S[j] = flip(S[j])
        i += 1

    if '-' in S:
        ans = "IMPOSSIBLE"
    else:
        ans = str(count)

    print("Case #" + str(testCase + 1) + ": " + ans)