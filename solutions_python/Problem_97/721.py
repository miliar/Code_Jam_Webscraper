def get_cycle(n, min_, max_):
    n_str = str(n)
    res = set()
    for i in range(1, len(n_str)):
       current = int(n_str[i:] + n_str[:i])
       if min_ <= current <= max_ and current != n:
           res.add(frozenset([n, current]))
    return res


def nbr_recycle(a, b):
    seen = set()
    count = 0
    i = a - 1
    while i < b:
        i += 1
        tmp = get_cycle(i, a, b)
        count += len(tmp.difference(seen))
        seen.update(tmp)
    return count


def main():
    t = int(raw_input())
    for i in range(t):
        a, b = map(int, raw_input().split())
        res = nbr_recycle(a, b)
        print 'Case #%d: %d' % (i + 1, res)


if __name__ == '__main__':
    main()
