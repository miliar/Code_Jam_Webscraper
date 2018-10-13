import sys
sys.stdin = open('input.in', 'r')
sys.stdout = open('output.out', 'w')


def output(s, k):
    n = 0
    i = 0

    while i < len(s) - k + 1:
        if s[i] == '-':
            n += 1

            for j in range(i, i+k):
                s[j] = '+' if s[j] == '-' else '-'

        i += 1

    possible = True

    for j in range(len(s)):
        if s[j] == '-':
            possible = False
            break

    if possible:
        return n

    return "IMPOSSIBLE"

T = int(input())

for i in range(T):
    line = input()
    [S, K] = line.split(" ")
    K = int(K)
    print("Case #" + str(i+1) + ": " + str(output(list(S), K)))
