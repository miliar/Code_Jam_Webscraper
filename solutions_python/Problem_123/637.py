def test_n(goal, now, mt):
    steps = 0
    ab = now
    while ab <= goal:
        ab = (ab << 1) - 1
        steps += 1
        if steps == mt:
            return mt, mt
    return steps, (ab + goal)


def inputer(file_name):
    in_file = open(file_name, 'r')
    cases = int(in_file.readline())
    for case in xrange(1, cases + 1):
        now, N = map(int, in_file.readline().split())
        motes = map(int, in_file.readline().split())
        yield now, motes, case


def solve(file_name, out_file_name):
    out_file = open(out_file_name, 'w')

    for now, motes, case in inputer(file_name):
        out_file.write('Case #%d: ' % case)
        times = 0
        motes.sort()
        sz = len(motes)

        for index in xrange(sz):

            if now > motes[index]:
                now += motes[index]
                continue

            t_times, nnow = test_n(motes[index], now, sz)

            if t_times < (sz - index):
                times += t_times
                now = nnow
            else:
                times += (sz - index)
                break

        out_file.write('%d\n' % times)

    out_file.close()


if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    solve(file_name, out_file_name)
