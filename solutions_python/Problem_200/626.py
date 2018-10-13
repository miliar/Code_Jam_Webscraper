import sys


T = int(sys.stdin.readline())
tests = []
for i in range(T):
    tests.append(int(sys.stdin.readline()))


def split(n):
    l = []
    while n > 0:
        l.insert(0, n % 10)
        n /= 10
    return l


def unsplit(l):
    p = 1
    res = 0
    for k in range(len(l)-1, -1, -1):
        res += l[k]*p
        p *= 10
    return res


def is_tidy(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


def first_index_not_tidy(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return i
    return None


def find_tidy(l):
    i = first_index_not_tidy(l)
    if i is None:
        return l
    if i > 0 and l[i] == 0:
        if l[i] == 0:
            l[i] = 9
            # l[i-1] != 0 because i first non tidy so l[i-1] > l[i] = 0
            l[i-1] -= 1
            # swap the remainder to 9
            for k in range(i+1, len(l)):
                l[k] = 9
            # we know that next non tidy is < i so terminates
            return find_tidy(l)
    else:
        # we know that l[0] > 0 so comes down to second case
        l[i] -= 1
        for k in range(i+1, len(l)):
            l[k] = 9
        # we know that next non tidy is < i so terminates
        return find_tidy(l)


# print decrement(split(111111111111111110))
# print is_tidy(decrement(split(111111111111111110)))

for nb, t in enumerate(tests):
    res = unsplit(find_tidy(split(t)))
    sys.stdout.write("Case #{}: {}\n".format(nb+1, res))
