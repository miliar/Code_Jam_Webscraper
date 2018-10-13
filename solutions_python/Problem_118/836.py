# http://code.activestate.com/recipes/577821-integer-square-root-function/
def isqrt(x):
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

# calculates the influences of n-digit palindrome to each digit of its square
def influences(n):
    v = [[] for i in xrange(n*2-1)]
    for i in xrange((n+1)/2):
        for j in xrange((n+1)/2):
            u = str((10**i + 10**(n-i-1) if i*2<n-1 else 10**i) *
                    (10**j + 10**(n-j-1) if j*2<n-1 else 10**j))
            for k in xrange(len(u)):
                v[k] += [tuple(sorted((i,j)))] * int(u[-1-k])
    return v

def check_if_middle_dominates_influences(n):
    infl = influences(n)
    assert infl[n-1] == [(i/2, i/2) for i in xrange(n)]
    for v in xrange(4**n):
        digits = [sum(((v>>(2*i))&3) * ((v>>(2*j))&3) for i,j in iinfl) for iinfl in infl]
        if max(digits) != digits[n-1]:
            assert False, 'assumption failed (v=%r digits=%r n=%r)' % (v, digits, n)

if 0:
    for i in xrange(1, 10):
        check_if_middle_dominates_influences(i)

def nsqpalins_upto_brute(k):
    count = 0
    for i in xrange(1, k+1):
        if str(i) == str(i)[::-1] and str(i*i) == str(i*i)[::-1]:
            #print '(brute', k, i, ")"
            count += 1
    return count

# so, we are sure that:
# - for even # of digits, abc...cba is fair and square iff a^2>0 and 2a^2+2b^2+...<10
# - for odd # of digits, abc..x..cba is fair and square iff a^2>0 and 2a^2+2b^2+...+x^2<10
# consequently, a should be one of 1 or 2, x should be 0, 1 or 2 (if any) and
# sum of squares of other digits should be less than 5 - a^2 - x^2/2.
# in particular, we can only have 0s or 1s in remaining digits.

def k_outof_n(n, k):
    v = 1
    for i in xrange(k): v = v * (n-i) / (i+1)
    return v

def nsumsq_upto_rec(n, sqlimit, limit): # limit should be the first (n+1)/2 digits
    if n == 0: return 1
    sigval = 10**(n-1)
    count = 0
    if limit == sigval*10-1:
        for i in xrange(sqlimit+1):
            if i <= n: count += k_outof_n(n, i)
    else:
        updigit, newlimit = divmod(limit, sigval)
        for digit in (0, 1):
            newsqlimit = sqlimit - digit*digit
            if newsqlimit >= 0:
                if digit < updigit:
                    count += nsumsq_upto_rec(n-1, newsqlimit, sigval-1)
                elif digit == updigit:
                    count += nsumsq_upto_rec(n-1, newsqlimit, newlimit)
    return count

def nsumsq_upto(n, sqlimit, limit):
    ret = nsumsq_upto_rec(n, sqlimit, limit)
    #print 'nsumsq_upto(%r, %r, %r) = %r' % (n, sqlimit, limit, ret)
    return ret

def nsqpalins_of_len_upto(n, limit):
    if n == 1: return len([i for i in [1, 2, 3] if i <= limit])
    if n == 2: return len([i for i in [11, 22] if i <= limit])

    sqn = (n+1)/2

    if limit >= 10**n:
        newlimit = 10**sqn - 1
    else:
        # for example, limit of 4059777 yields new limit of 4059,
        # but limit of 4059333 yields new limit of 4058
        # since largest palindrome up to 4059333 is 4058504.
        newlimit = int(str(limit)[:(n+1)/2])
        if str(limit)[:n/2][::-1] > str(limit)[-(n-1)/2:]: newlimit -= 1

    odd = (n%2 == 1)
    freedom = n/2-1 # 3 digit has zero freedom, 4-5 digit has one freedom, ..
    sigval = 10**(sqn-1)

    count = 0

    # handle the cases if a=1
    if newlimit >= 2 * sigval:
        # a=1 x=0 sqlimit=3
        count += nsumsq_upto(freedom, 3, sigval-1)
        if odd:
            # a=1 x=1 sqlimit=2
            count += nsumsq_upto(freedom, 2, sigval-1)
            # a=1 x=2 sqlimit=1
            count += nsumsq_upto(freedom, 1, sigval-1)
    elif newlimit >= sigval:
        if odd:
            # a=1 x=0 sqlimit=3
            freedomlimit = newlimit % sigval / 10
            if freedomlimit >= 0: count += nsumsq_upto(freedom, 3, freedomlimit)
            # a=1 x=1 sqlimit=2
            freedomlimit = newlimit % sigval / 10
            if newlimit % 10 < 1: freedomlimit -= 1
            if freedomlimit >= 0: count += nsumsq_upto(freedom, 2, freedomlimit)
            # a=1 x=2 sqlimit=1
            freedomlimit = newlimit % sigval / 10
            if newlimit % 10 < 2: freedomlimit -= 1
            if freedomlimit >= 0: count += nsumsq_upto(freedom, 1, freedomlimit)
        else:
            # a=1 x=0 sqlimit=3
            count += nsumsq_upto(freedom, 3, newlimit % sigval)

    # handle the cases if a=2
    if newlimit >= 3 * sigval:
        # a=2 x=0 sqlimit=0
        count += nsumsq_upto(freedom, 0, sigval-1)
        if odd:
            # a=2 x=1 sqlimit=0
            count += nsumsq_upto(freedom, 0, sigval-1)
    elif newlimit >= 2 * sigval:
        if odd:
            # a=2 x=0 sqlimit=0
            freedomlimit = newlimit % sigval / 10
            if freedomlimit >= 0: count += nsumsq_upto(freedom, 0, freedomlimit)
            # a=2 x=1 sqlimit=0
            freedomlimit = newlimit % sigval / 10
            if newlimit % 10 < 1: freedomlimit -= 1
            if freedomlimit >= 0: count += nsumsq_upto(freedom, 0, freedomlimit)
        else:
            # a=2 x=0 sqlimit=0
            count += nsumsq_upto(freedom, 0, newlimit % sigval)

    return count

if 0:
    print nsqpalins_of_len_upto(1, 999999), nsqpalins_upto_brute(9)
    print nsqpalins_of_len_upto(2, 999999), nsqpalins_upto_brute(99)
    print nsqpalins_of_len_upto(3, 999999), nsqpalins_upto_brute(999)
    print nsqpalins_of_len_upto(4, 999999), nsqpalins_upto_brute(9999)
    print nsqpalins_of_len_upto(5, 999999), nsqpalins_upto_brute(99999)
    print nsqpalins_of_len_upto(6, 999999), nsqpalins_upto_brute(999999)

cache = {}
def nsqpalins_upto(limit):
    limit = isqrt(limit)
    if limit in cache: return cache[limit]

    n = 1
    tens = 1
    count = 0
    while limit >= tens:
        ret = nsqpalins_of_len_upto(n, limit)
        #print 'nsqpalins_of_len_upto(%r, %r) = %r' % (n, limit, ret)
        count += ret
        n += 1
        tens *= 10

    cache[limit] = count
    #print 'nsqpalins_upto(%r) = %r' % (limit, count)
    if 0:
        expected = nsqpalins_upto_brute(limit)
        assert count == expected, (limit, count, expected)
    return count

if 0:
    import random
    selected = [1, 4, 10, 100, 120, 1000, 14400, 77777, 1727307**2, 2246414**2]
    selected += [random.randint(1, 10000000000000) for i in xrange(10)]
    selected += [random.randint(1, 1000000000000000) for i in xrange(3)]
    for i in selected: nsqpalins_upto(i)

ncases = int(raw_input())
for caseno in xrange(1, ncases+1):
    a, b = map(int, raw_input().split())
    count = nsqpalins_upto(b) - nsqpalins_upto(a-1)
    print 'Case #%d: %d' % (caseno, count)

