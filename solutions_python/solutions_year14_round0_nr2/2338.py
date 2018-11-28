def diff_from_prev(c, f, x, n):
    return c / (2 + f*(n-1)) - (x*f) / ((2+n*f)*(2+n*f-f))

def get_best_time(c, f, x):
    prev_time = x / 2
    k = 1
    d = diff_from_prev(c, f, x, k)
    time = d + prev_time
    while time < prev_time:
        prev_time = time
        k += 1
        d = diff_from_prev(c, f, x, k)
        time = d + prev_time
    return prev_time

for i in range(input()):
    c, f, x = map(float, raw_input().split())
    print 'Case #%d: %f' % (i+1, get_best_time(c, f, x))
