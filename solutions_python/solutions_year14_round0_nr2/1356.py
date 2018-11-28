import sys

def run_case(c, f, x):

    freq = 2
    ammount = 0
    time = 0

    while True:
        # whether the total amount of time of buying a farm
        # and waiting for completion is bigger then just waiting
        # for completion.
        if c / freq + x / (freq + f) > x / freq:
            time += x / freq
            break

        time += c / freq
        freq += f

    return time


def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    for case in range(int(lines[0])):
        c, f, x = lines[case + 1].split()
        print('Case #{}: {:7f}'.format(
            case + 1,
            run_case(float(c), float(f), float(x)))
        )

if __name__ == '__main__':
    main()