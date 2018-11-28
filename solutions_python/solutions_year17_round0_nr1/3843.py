def read(f):
    lines = open(f, 'r').read().split('\n')
    for line in lines[1:]:
        if len(line):
            yield line.split()


def solve(task):
    length = len(task[0])
    S = int(task[0].replace('-', '0').replace('+', '1'), 2)
    K = int(task[1])
    m = 2 ** K - 1
    steps = 0
    while length > K:
        if S & 1 == 0:
            S ^= m
            steps += 1
        S >>= 1
        length -= 1
    if S == 0:
        return steps + 1
    if S == m:
        return steps

    return 'IMPOSSIBLE'


def output(tasks):
    for i, task in enumerate(tasks, start=1):
        print 'Case #' + str(i) + ':', solve(task)


def check(tasks):
    for task in tasks:
        assert str(solve(task)) == task[2], 'S=%s K=%s E=%s A=%s' % (task[0], task[1], task[2], solve(task))


output(read('codejam001_sa.txt'))


# check(read('codejam001_example.txt'))
