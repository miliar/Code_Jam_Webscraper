import sys
sys.stdout = open('b_big.out', 'w')
sys.stdin  = open("b_big.in", 'r')
T = int(raw_input())


def tidy(s):
    return s == sorted(s)



def algorithm(N):
    s = map(int, list(str(N)))
    if tidy(s):
        return N
    L = len(s)
    for i in range(L - 1, 0, -1):
        if s[i] < s[i - 1]:
            if s[i - 1] != 0:
                s[i - 1] -= 1
                for k in range(i, L):
                    s[k] = 9
            else:
                for k in range(i, L):
                    s[k] = 0

    return str(int("".join(map(str, s))))


def solve():
    N = int(raw_input())
    return algorithm(N)

for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)