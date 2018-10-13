from functools import wraps

def memorize(func):
    cache = dict()

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memorize
def cal(n, c, f):
    if n == 0:
        return 0.0
    return cal(n-1, c, f) + c * 1.0 / (2 + f*(n-1))

T = input()
for cas in xrange(T):
    c, f, x = map(float, raw_input().split())
    res = x / 2.0
    for n in xrange(int(x)):
        res = min(res, cal(n, c, f) + x / (2 + n*f))
    print 'Case #{0}:'.format(cas+1), res
