# Daniel Balle 2017
#
# Tidy Numbers
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

def greedy(n, i):
    # fix n[i] and n[i+1] - we return true if we had to change n[i+1]
    if n[i] > n[i+1]:
        n[i] -= 1
        return True

    return False



T = int(raw_input().strip())
for t in range(1, T+1):

    n = map(int, list(raw_input().strip()))
    first_nine = len(n)

    for i in range(len(n) - 2, 0 - 1, -1):
        first_nine = i + 1 if greedy(n, i) else first_nine

    # transform all those nines
    for i in range(first_nine, len(n)):
        n[i] = 9

    tidy = int(''.join( str(x) for x in n ))
    print "Case #{}: {}".format(t, tidy)
