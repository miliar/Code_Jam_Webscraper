# Bathroom Stalls


def append_to_state(state, l, c):
#    print("called")
#    print("(with state %s)" % state)
    # TODO: a priority queue or similar would greatly help
    for i in range(len(state)):
        if state[i][0] == l:
            state[i][1] += c
            return(state)
        elif state[i][0] < l:
            state = state[:i] + [[l, c]] + state[i:]
            return(state)
    state.append([l, c])
    return(state)


def simulate_entries(cells, guests):
    # ends up with a description of the "battleground" afterwards
    # for debugging purposes
    # vocabulary override: stall -> cell

    # each state is described as a sequence of
    # (length, count) pairs, length being the number of cells in each stripe
    # of free cells,
    # more precisely:
    # [(l1, c1), (l2, c2), ..., (lk, ck)] where li > lj if i < j.

    # obvious: the next guest always goes for one of the longest stripes
    # obvious: the next c1 guests will use up the l1 long stripes first

    # an l1 long stripe cracks up to
    # a floor((l1 - 1) / 2) and a ceil((l1 - 1) / 2) long stripe

    # so:

    state = [[cells, 1]]
    while guests > 0:
        l1 = state[0][0]
        c1 = state[0][1]
        takein = min(c1, guests)
        guests -= takein
        if c1 == takein:
            # l1 is entirely consumed, so
            state = state[1:]
        else:
            state[0][1] = c1 - takein
        # lesser half: integer division
        l1_2 = ((l1 - 1) / 2)
        l1_1 = (l1 - 1) - l1_2
#        print("%d x %d was split to %d and %d" % (l1, c1, l1_1, l1_2))
        if l1_1 > 0:
            # state.append([l1_1, takein])
            state = append_to_state(state, l1_1, takein)
            if l1_2 > 0:
                # state.append([l1_2, takein])
                state = append_to_state(state, l1_2, takein)
    return(state)


def get_last_neighbours(cells, guests):
    state = simulate_entries(cells, guests - 1)
    mi = (state[0][0] - 1) / 2
    mx = state[0][0] - 1 - mi
    return((mx, mi))


if __name__ == "__main__":
    # for i in range(100):
    #     get_last_neighbours(1000000000000000000, 1000000000000000000 - 1)

    test_count = int(raw_input())
    for case_index in range(test_count):
        cells, guests = [int(x) for x in raw_input().split()]
        mx, mi = get_last_neighbours(cells, guests)
        print("Case #%d: %d %d" % (case_index + 1, mx, mi))

    # print(simulate_entries(1000000000000000000, 1000000000000000000 - 1))
    # print(simulate_entries(1000000000000000000, 1000000000000000000 - 1))
    # state = [[3, 5], [1, 3]]
    # print(append_to_state(state, 5, 5))
