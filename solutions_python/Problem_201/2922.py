#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-


# occupied = 1, free = 0
def bathroom_stalls(N, K, verbose=False):

    if N == K:
        return (0, 0)

    stalls = [1] + [0] * N + [1]

    unoccupied_indices = set(range(1, N + 1))

    ls = {i: i for i in range(1, N + 1)}
    rs = {i: N + 1 - i for i in reversed(range(1, N + 1))}

    if verbose:
        print("LS:", sorted(ls.items()), "RS:", sorted(rs.items()))

    for _ in range(K):
        stall_index, l, r = next(iter(sorted(((index, ls[index], rs[index])
                                      for index in unoccupied_indices),
                                      key=lambda t: (min(t[1], t[2]), max(t[1], t[2]), -t[0]),
                                      reverse=True)))
        if verbose:
            print("INSERT IN STALL:", stall_index)

        stalls[stall_index] = 1

        from itertools import count
        left, right = True, True
        for cnt in count(1):

            if stalls[stall_index + cnt]:
                left = False

            if stalls[stall_index - cnt]:
                right = False

            if left:
                ls[stall_index + cnt] = cnt

            if right:
                rs[stall_index - cnt] = cnt

            if not (left or right):
                break

        if verbose:
            for i in ls.keys():
                print(i, "LS:", ls[i], "RS:", rs[i])

        unoccupied_indices -= {stall_index}

    return max(l, r) - 1, min(l, r) - 1


def main():
    import sys
    filename = sys.argv[1]

    with open(filename, "r") as infile:
        with open(filename.replace(".in", ".out"), "w") as outfile:
            inputs = [map(int, line.strip().split()) for line in
                      infile.readlines()[1:]]

            for i, inp in enumerate(inputs, 1):
                output = bathroom_stalls(*inp)
                outfile.write("Case #{}: {} {}\n".format(i, output[0], output[1]))


if __name__ == "__main__":
    main()
