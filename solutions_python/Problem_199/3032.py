def flip_pancake(c):
    if c == '-': return '+'
    if c == '+': return '-'


def flip_row(j):
    for k in range(K):
        S[j + k] = flip_pancake(S[j + k])


def has_flipped_pancake():
    for q in range(len(S)):
        if S[q] == '-':
            return True
    return False

T = int(input())
for i in range(T):
    line = input().split(" ")
    S = list(str(line[0]))
    K = int(line[1])
    c = 0
    for j in range(len(S) - K + 1):
        if S[j] == '-':
            c += 1
            flip_row(j)
    if has_flipped_pancake():
        print("Case #" + str(i + 1) + ": IMPOSSIBLE")
    else:
        print("Case #" + str(i + 1) + ": " + str(c))