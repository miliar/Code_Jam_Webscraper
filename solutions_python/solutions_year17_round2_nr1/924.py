import sys
import fileinput


def solve_next(stream):
    destination, horses = map(int, stream.readline().split())
    horse_props = (tuple(map(int, stream.readline().split()))
                   for _ in range(horses))
    etas = ((destination - initial) / max_speed
            for initial, max_speed in horse_props)
    max_speed = destination / max(etas)
    return max_speed


def main():
    with fileinput.input() as f:
        num_cases = int(f.readline())
        for index in range(1, num_cases + 1):
            solution = solve_next(f)
            print("Case #{}: {}".format(index, solution))


if __name__ == "__main__":
    sys.exit(main())
