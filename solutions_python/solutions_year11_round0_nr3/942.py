import sys

def read_data():
    with open(sys.argv[1]) as f:
        test_count = int(f.readline())
        for t in xrange(test_count):
            f.readline()
            yield (t+1, [int(n) for n in f.readline().split()])

def solve(data):
    t_num, numbers = data
    xsum = 0
    S = 0
    min_ = numbers[0]
    for n in numbers:
        xsum ^= n
        S += n
        if min_ > n:
            min_ = n
    if xsum == 0:
        print "Case #%d: %d" % (t_num, (S - min_))
    else:
        print "Case #%d: NO" % t_num
if __name__ == '__main__':
    for test in read_data():
        solve(test)
