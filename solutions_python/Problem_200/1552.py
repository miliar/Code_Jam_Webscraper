import sys

total = None
cases = 0

def is_tidy(n):
    t = str(n)

    for idx, c in enumerate(t):
        if idx > 0:
            if t[idx] < t[idx-1]:
                return False

    return True


def test(n):

    if n < 10:
        return n

    while is_tidy(n) == False:
        #if n % 10 == 0:
        #    n = n - (n/10)
        #else:
            n = n-1

    return n


for line in sys.stdin:
    if total:
        cases = cases+1
        res = str(test(int(line)))
        sys.stdout.write('Case #' + str(cases) + ': ' + res + '\n')
    else:
        total = line
