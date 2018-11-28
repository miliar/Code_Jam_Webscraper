T = input()
for t in range(T):
    cnt = 0
    N = input()
    num = map(int, raw_input().split())

    if len(num) != len(set(num)):
        raise Exception()
    num_s = sorted(num)

    for turn in num_s:
        idx = num.index(turn)
        a = min(idx, len(num) - idx - 1)
        cnt += a
        num.pop(idx)

    print 'Case #%d:' % (t+1), cnt
