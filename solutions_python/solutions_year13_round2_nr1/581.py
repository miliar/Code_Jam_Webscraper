import sys

def solve_case(A, N, motes):
    # print A, N, sorted(motes)
    if A == 1:
        return N

    mote_index = [0] * 101
    for m in motes:
        mote_index[m] = mote_index[m] + 1

    # How many motes to delete to make solvable?
    deletable_motes = len(motes)
    added_motes = 0
    # List of num_motes_added + num_motes_deleted
    options = []
    i = 1
    while i <= 100:
        if mote_index[i] == 0:
            i = i + 1
        elif A > i:
            A = A + (i * mote_index[i])
            deletable_motes = deletable_motes - mote_index[i]
            i = i + 1
        else:
            # Ok, we have the choice of deleting the rest, or adding a mote
            options.append(added_motes + deletable_motes)
            A = A + (A - 1)
            added_motes = added_motes + 1

    options.append(added_motes)

    # print options
    if options:
        return min(options)
    else:
        return 0

if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().strip())

    for c_n in xrange(num_cases):
        A, N = map(int, sys.stdin.readline().strip().split())
        motes = map(int, sys.stdin.readline().strip().split())
        min_moves = solve_case(A, N, motes)
        print "Case #%d: %d" % (c_n+1, min_moves)
