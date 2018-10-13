import argparse
import sys

def get_speed(dest, others):
    """Gets the best speed to ride."""
    time = max(
        (dest - loc) / speed
        for loc, speed in others
    )
    return dest / time


def main():
    """The main driver."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', type=argparse.FileType('r'), 
        default=sys.stdin
    )
    args = parser.parse_args()
    inp = args.input

    n_test_cases = int(inp.readline())
    for test_case in range(n_test_cases):
        header = inp.readline().split()
        dest = float(header[0])
        n_others = int(header[1])
        others = []
        for _ in range(n_others):
            others.append(tuple(
                float(i) for i in inp.readline().split()
            ))
            continue
        speed = get_speed(dest, others)

        print('Case #{}: {}'.format(test_case + 1, speed))
        continue


if __name__ == '__main__':
    main()

