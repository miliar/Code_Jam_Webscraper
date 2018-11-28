import sys


def solve(switches, flipper):
    idx = 0
    moves = 0
    while idx <= len(switches) - flipper:
        if not switches[idx]:
            moves += 1
            for i in range(flipper):
                switches[idx + i] = not switches[idx + i]

        try:
            idx = switches.index(False, idx)
        except ValueError:
            return moves

    return 'IMPOSSIBLE'


def main():
    fni = sys.argv[1]

    with open(fni) as fi:
        fi.readline()
        for idx, line in enumerate(fi):
            switches, flipper_str = line.strip().split(' ')
            switches = [c == '+' for c in switches]
            flipper = int(flipper_str)
            solution = solve(switches, flipper)
            print('Case #{}: {}'.format(idx + 1, solution))


if __name__ == '__main__':
    main()