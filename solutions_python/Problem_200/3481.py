
def tidy(n):
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True

def tidy_nums(n):
    n = map(int, list(str(n)))
    n = list(n)
    i = len(n) - 1

    while not tidy(n):
        a = n[i - 1]
        n[i - 1] = a - 1
        n[i] = 9
        i -= 1
    n = map(str, n)
    n = list(n)
    return int(''.join(n))

with open('tidy.in') as f:
    f.readline()
    for i, line in enumerate(f):
        n = int(line.strip())
        ans = tidy_nums(n)
        print('case #%s: %s' % (i+1, ans))
