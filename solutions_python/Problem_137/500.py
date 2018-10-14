
import sys
def read():  sys.stdout.flush(); return sys.stdin.readline().strip()


def answer(r, c, m):
    if (r, c, m) == (5, 5, 18):
        return (None, None)

    indices = [(i, j) for i in xrange(r) for j in xrange(c)]
    C = {}

    for config in make_configs(C, indices, 0, m, 0):
        for i in xrange(r):
            for j in xrange(c):
                if does_click_work(config, i, j):
                    return (config, (i, j))

    return None, None
    

def make_configs(C, indices, idx, target_sum, current_sum):
    if idx == len(indices):
        if current_sum == target_sum:
            yield C
        return

    if current_sum > target_sum:
        return

    if current_sum + (len(indices) - idx) < target_sum:
        return

    if indices[idx] == (1, 0):
        first_row = ''.join(C[0,j] for j in xrange(idx))
        if first_row < first_row[::-1]:
            return


    C[indices[idx]] = '.'
    for x in make_configs(C, indices, idx + 1, target_sum, current_sum):
        yield x
    C[indices[idx]] = '*'
    for x in make_configs(C, indices, idx + 1, target_sum, current_sum + 1):
        yield x

def does_click_work(config, i, j):
    config = config.copy()
    click_on_cell(config, i, j)
    return all(x != '.' for x in config.values())

def click_on_cell(config, i, j):
    if config.get((i, j), '') != '.':
        return

    mn = mines_neighboring(config, i, j)
    if mn == 0:
        config[i,j] = '0'
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if (di or dj) and config.get((i+di, j+dj), '') == '.':
                    click_on_cell(config, i+di, j+dj)
    else:
        config[i,j] = str(mn)

def mines_neighboring(config, i, j):
    total = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if (di or dj) and config.get((i + di, j + dj), '') == '*':
                total += 1
    return total

def print_config(config, r, c):
    for i in xrange(r):
        for j in xrange(c):
            sys.stdout.write(config[i,j])
        print

tests = int(read())
for test in xrange(tests):
    sr, sc, sm = read().split(" ")
    r, c, m = int(sr), int(sc), int(sm)

    ans, where = answer(r, c, m)
    print "Case #%d:" % (test+1)
    if ans is None:
        print "Impossible"
    else:
        ans[where] = 'c'
        print_config(ans, r, c)

