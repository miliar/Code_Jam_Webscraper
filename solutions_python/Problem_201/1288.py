def round_up(n):
    x = n - 1
    i = 1
    while i < n:
        x = x | (x >> i)
        i *= 2
    return x + 1

for t in xrange(1, input() + 1):
    n, k = map(int, raw_input().split())
    reps = round_up(k + 1) / 2
    qty = n - k + 1
    free = (qty / reps)
    if qty % reps:
        free += 1
    min_choice = free / 2
    max_choice = free / 2
    if not free % 2 and free > 1:
        min_choice -= 1

    print 'Case #%d: %d %d' % (t, max_choice, min_choice)
