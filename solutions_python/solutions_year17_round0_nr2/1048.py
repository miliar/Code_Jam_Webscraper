import sys


def is_tidy(N):
    if len(N) == 1:
        return True
    for i in range(1, len(N)):
        if N[i - 1] > N[i]:
            return i - 1
    else:
        return True


def rm_leading_zero(N):
    while N.startswith('0'):
        if N == '0':
            return '0'
        N = N[1:]
    return N


def solve(N):
    while True:
        N = rm_leading_zero(N)
        check = is_tidy(N)
        if type(check) is bool and check == True:
            return N
        new = N[:check] + str(int(N[check]) - 1) + '9' * (len(N) - check - 1)
        N = new


with open(sys.argv[1], "r") as f:
    file = f.readlines()
    T = int(file.pop(0))
    for t in range(T):
        N = str(file.pop(0).strip())
        print "Case #%d: %s" % (t + 1, solve(N))
