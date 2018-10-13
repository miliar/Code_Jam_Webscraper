
def get_chunk():
    f = open('input1.txt')
    line = f.readline()
    while line:
        line = f.readline()
        if not line:
            break
        N, _ = [int(x) for x in line.split(' ')]
        line = f.readline()
        SIZES = [int(x) for x in line.split(' ')]
        yield (N, SIZES)


def solve(chunk):
    N, SIZES = chunk
    SIZES.sort()
    operations = 0
    # print N, SIZES
    for index, x in enumerate(SIZES):
        if N > x:
            N += x
        else:
            old = operations
            oldN = N
            mustbreak = False
            iterations = 0
            if N == 1:
                operations += 1
                continue
            while N <= x:
                N += N - 1
                operations += 1
                iterations += 1
                # print 'ops: ', operations
                # print 'index: ', index
                if iterations >= len(SIZES) - index + 1:
                    operations = old + 1
                    N = oldN
                    mustbreak = True
                    break
            if mustbreak:
                continue
            N += x
        if operations > len(SIZES):
            return len(SIZES)
    return operations

for index, chunk in enumerate(get_chunk()):
    print 'Case #%s:' % (index + 1), solve(chunk)
    # break
