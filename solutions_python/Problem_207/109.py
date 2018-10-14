import sys


def get_input(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            [N, R, O, Y, G, B, V] = [int(x) for x in f.readline().split()]
            cases.append([N, R, O, Y, G, B, V])
        return T, cases


def print_output(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            line = "Case #{0}: {1}".format(t+1, res[t])
            print(line)
            f.write(line + "\n")


def find_arrangement_simple(s):
    [N, R, O, Y, G, B, V] = s
    unicorns = [R, Y, B]
    arrangement = []
    if R > 0:
        arrangement.append('R')
        unicorns[0] -= 1
    elif Y > 0:
        arrangement.append('Y')
        unicorns[1] -= 1
    else:
        arrangement.append('B')
        unicorns[2] -= 1

    for n in range(N-1):
        if arrangement[n] == 'R':
            if unicorns[1] == 0 and unicorns[2] == 0:
                return "IMPOSSIBLE"
            elif unicorns[1] >= unicorns[2]:
                arrangement.append('Y')
                unicorns[1] -= 1
            else:
                arrangement.append('B')
                unicorns[2] -= 1
        elif arrangement[n] == 'Y':
            if unicorns[0] == 0 and unicorns[2] == 0:
                return "IMPOSSIBLE"
            elif unicorns[0] >= unicorns[2]:
                arrangement.append('R')
                unicorns[0] -= 1
            else:
                arrangement.append('B')
                unicorns[2] -= 1
        else:
            if unicorns[0] == 0 and unicorns[1] == 0:
                return "IMPOSSIBLE"
            elif unicorns[0] >= unicorns[1]:
                arrangement.append('R')
                unicorns[0] -= 1
            else:
                arrangement.append('Y')
                unicorns[1] -= 1

    if arrangement[0] == arrangement[-1]:
        return "IMPOSSIBLE"

    return arrangement


def find_arrangement(s):
    [N, R, O, Y, G, B, V] = s

    if G > R or V > Y or O > B:
        return "IMPOSSIBLE"
    elif G == R and G>0:
        if N > G + R:
            return "IMPOSSIBLE"
        else:
            return G * "GR"
    elif V == Y and V>0:
        if N > V + Y:
            return "IMPOSSIBLE"
        else:
            return V * "VY"
    elif O == B and O>0:
        if N > O + B:
            return "IMPOSSIBLE"
        else:
            return O * "OB"

    arrangement = find_arrangement_simple([R+Y+B-G-V-O, R-G, O, Y-V, G, B-O, V])

    if arrangement == "IMPOSSIBLE":
        return "IMPOSSIBLE"

    if G>0:
        red_unicorn_index = arrangement.index('R')
        arrangement[red_unicorn_index] = G * 'RG' + 'R'
    if V>0:
        yellow_unicorn_index = arrangement.index('Y')
        arrangement[yellow_unicorn_index] = V * 'YV' + 'Y'
    if O>0:
        blue_unicorn_index = arrangement.index('B')
        arrangement[blue_unicorn_index] = O * 'BO' + 'B'

    return "".join(arrangement)

if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    T, cases = get_input(input_filename)
    res = [find_arrangement(s) for s in cases]
    print_output(res, T, output_filename)
