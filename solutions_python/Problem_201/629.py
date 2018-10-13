f = open('C-large.in')
fw = open('C-large.out', 'w')

T = int(f.readline())
for t in xrange(T):
    N, K = map(int, f.readline().split())
    count = 0
    div = 1
    while count < K:
        count += div
        div *= 2
    order = K - (count - (div / 2))
    res = (N - count) % div
    _max = (N - count) / div
    _min = (N - count) / div
    _max += 1 if order <= res else 0
    _min += 1 if order <= res - (div / 2) else 0

    fw.write('Case #' + str(t + 1) + ': ')
    fw.write(str(_max) + ' ' + str(_min) + '\n')

fw.close()
f.close()
