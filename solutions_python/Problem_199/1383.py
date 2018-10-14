import sys
input = open(sys.argv[1])


def fit(s, k, g):
    ss = s
    s = [0 if x == '-' else 1 for x in list(s)]
    for i in range(len(s) - k + 1):
        if (g >> i) & 1:
            for j in range(k):
                s[i + j] += 1
    if all([x % 2 for x in s]):
        print (k, ss, s)
    return all([x % 2 for x in s])


def solve(s, k):
    k = int(k)
    s = [0 if x == '-' else 1 for x in list(s)]
    ans = 0
    for i in range(len(s) - k + 1):
        if s[i] == 0:
            ans += 1
            for j in range(k):
                s[i + j] = not s[i + j]
    return ans if all(s) else 'IMPOSSIBLE'


for case in range(int(input.readline())):
    s, k = input.readline().split()
    print ("Case #%d: %s" % (case + 1, solve(s, k)))
