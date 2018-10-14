#! python3

DATA_FILE = "C-large"

def main():
    with open(DATA_FILE + ".in") as in_file:
        with open(DATA_FILE + ".out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '')
                N, K = [int(i) for i in line.split()]

                if N == K:
                    fout.write("Case #{0}: {1} {2}\n".format(x + 1, 0, 0))
                    continue

                total_people = 0
                level_people = 1
                space_count = { N: 1 }
                while total_people + level_people < K:
                    total_people += level_people
                    space_count = split(space_count)
                    level_people <<= 1

                level_people_left = K - total_people
                high_space = max(space_count.keys())
                low_space = min(space_count.keys())
                if level_people_left <= space_count[high_space]:
                    split_space = high_space
                else:
                    split_space = low_space

                new_spaces = sorted(split({split_space: 1}, include_zero=True).keys(), reverse=True)
                if len(new_spaces) == 2:
                    max_left, min_left = new_spaces
                else:
                    max_left, min_left = new_spaces[0], new_spaces[0]

                fout.write("Case #{0}: {1} {2}\n".format(x + 1, max_left, min_left))

def split(space_count, include_zero=False):
    new_space_count = {}

    for space, count in space_count.items():
        new_space = space // 2
        new_space_b = space // 2 - 1
        if space % 2 == 0:
            new_space_count[new_space] = new_space_count.get(new_space, 0) + count
            if new_space_b > 0 or include_zero and new_space_b >= 0:
                new_space_count[new_space_b] = new_space_count.get(new_space_b, 0) + count
        else:
            if new_space > 0 or include_zero and new_space <= 0:
                new_space_count[new_space] = new_space_count.get(new_space, 0) + count * 2
    return new_space_count

if __name__ == "__main__":
    main()
