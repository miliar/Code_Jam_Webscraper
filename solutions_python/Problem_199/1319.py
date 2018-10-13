def process():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        p, w = [s for s in input().split(" ")]
        window_size = int(w)
        pancakes = [-1 if s == '-' else 1 for s in p]
        flips = get_flips(pancakes, window_size)
        print("Case #{}: {}".format(i, flips))


def get_flips(pancakes, window_size):
    total_flips = 0
    for i in range(0, len(pancakes)):
        if pancakes[i] == -1:
            if i > len(pancakes) - window_size:
                return 'IMPOSSIBLE'
            else:
                do_flips(pancakes, i, window_size)
                total_flips += 1
    return total_flips


def do_flips(pancakes, start_index, window_size):
    for i in range(start_index, start_index + window_size):
        pancakes[i] *= -1


if __name__ == "__main__":
    process()
