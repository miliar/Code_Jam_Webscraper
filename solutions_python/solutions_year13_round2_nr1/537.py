import sys

def read_int(fp=sys.stdin):
    return int(fp.readline().strip())

def read_ints(fp=sys.stdin):
    return map(int, fp.readline().strip().split())

def count_left(mote, motes):
    while motes and motes[0] < mote:
        mote += motes[0]
        motes = motes[1:]
    return len(motes)

def solve_level(mote, motes):
    # Not possible to add something, remaining actions are all remove.
    if mote == 1:
        return len(motes)

    if not motes:
        return 0

    # Eat all we can
    if motes[0] < mote:
        while motes and motes[0] < mote:
            mote += motes[0]
            motes = motes[1:]

    if not motes:
        return 0

    count_add = solve_level(mote, [mote - 1] + motes)
    count_remove = solve_level(mote, motes[:-1])
    return min(count_add, count_remove) + 1

if __name__ == "__main__":
    T = read_int()
    for t in range(1, T+1):
        A, N = read_ints()
        motes = read_ints()
        motes.sort()

        count = solve_level(A, motes)
        print "Case #%d: %d" % (t, count)
