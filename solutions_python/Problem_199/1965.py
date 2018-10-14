def parse_test(line):
    line = line.strip()
    args = line.split(" ")
    return (args[0], int(args[1]))

def clear_ones(pancakes):
    while len(pancakes) > 0 and pancakes[0] == 1:
        pancakes.pop(0)
    return pancakes
with open("A-large.in") as ifile, open("pancake.out", "w") as ofile:
    T = int(ifile.readline().strip())
    for testnum in range(T):
        ofile.write("Case #{}: ".format(testnum + 1))
        flips = 0
        line = ifile.readline()
        pancakes, flipper = parse_test(line)

        deque = []
        while len(pancakes) > 0:
            while len(deque) < flipper and len(pancakes) > 0:
                if pancakes[0] == '-':
                    deque.append(-1)
                else:
                    deque.append(1)
                pancakes = pancakes[1:]
            deque = clear_ones(deque)

            if len(deque) == flipper:
                flips += 1
                deque = [-x for x in deque]
                deque = clear_ones(deque)

        if len(deque) == 0:
            ofile.write("{}\n".format(flips))
        else:
            ofile.write("IMPOSSIBLE\n")