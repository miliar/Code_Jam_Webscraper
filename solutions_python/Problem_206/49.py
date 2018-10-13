

def proc(case):
    case += 1
    d, n = map(lambda x: int(x), raw_input().split())
    spend = 0.0
    for i in xrange(n):
        start, speed = map(lambda x: int(x), raw_input().split())
        spend = max(spend, (d - start) / float(speed))
    print 'Case #{}: {:.6f}'.format(case, d / spend)


def run():
    n = int(raw_input())
    for i in xrange(n):
        proc(i)


if __name__ == '__main__':
    run()
