import sys
def i_to_lst(i, radix=10):
    """Return a list of the digits in i, i>0"""
    acc = []
    while i > 0:
        acc.insert(0, i % radix)
        i /= radix
    return acc

def lst_to_i(lst, radix=10):
    """Make an integer out of the digits in lst. Each element in lst < radix"""
    return reduce(lambda a, d: a * radix + d, lst, 0)

def num_digits(n, radix=10):
    return len(str(n))

def recycle(n):
    n_lst = i_to_lst(n)
    i = len(n_lst) - 1
    while i > 0:
        r_lst = n_lst[-i:] + n_lst[:-i]
        if r_lst[0] != 0 and num_digits(lst_to_i(r_lst)) == num_digits(lst_to_i(n_lst)):
            yield lst_to_i(r_lst)
        i-=1

def count_pairs(a, b, n, pairs):
    count = 0
    for m in recycle(n):
        if m <= b and n >= a and m > n:
            if (n, m) not in pairs:
                pairs.add((n,m))
                count += 1
    return count

def f(a,b, pair_set):
    pairs = 0
    for n in xrange(a, b+1):
        pairs += count_pairs(a,b,n, pair_set)
    return pairs

n = int(sys.stdin.readline())
for i in xrange(1, n+1):
    a, b = [int(j) for j in sys.stdin.readline().split()]
    pset = set()
    print "Case #" + str(i) + ": " + str(f(a, b, pset))
