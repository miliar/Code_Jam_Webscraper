

def solve_test(line, g):

    # print
    pancakes, k = line.split()
    k, heads    = int(k), []

    def swap(pancake):
        if pancake == '-':
            return '+'
        else:
            return '-'

    swap_count = 0

    for idx, pancake in enumerate(pancakes):

        if len(heads) > 0:
            l, r = heads[0]
            if l <= idx <= r:
                pancake = swap(pancake)
            elif idx > r:
                heads.pop(0)

        # print idx, pancake, heads

        if pancake == '-':

            # print "Trigger swap"

            swap_count += 1
            next_pos = idx + k  - 1

            if next_pos >= len(pancakes):
                g.write("IMPOSSIBLE")
                return

            if len(heads) == 0:
                heads.append((idx, next_pos))
            else:

                new_heads = []

                # print "Computing new heads"

                cidx = idx
                for jdx, head in enumerate(heads):

                    l, r = head

                    if cidx >= l:
                        cidx = r + 1
                        continue
                    else:
                        # print "new head: ", cidx, l - 1
                        new_heads.append((cidx, l - 1))
                    #
                    # print "jump to ", r + 1
                    cidx = r + 1

                new_heads.append((cidx, next_pos))
                heads = new_heads

        # print heads

    g.write(str(swap_count))


def solve(file):

    with open(file) as f:
        with open("res", "w") as g:
            for idx, line in enumerate(f.readlines()[1:]):
                g.write("Case #" + str(idx + 1) + ": ")
                solve_test(line, g)
                g.write("\n")


def main():
    solve("pancake.in")


if __name__ == "__main__":
    main()


