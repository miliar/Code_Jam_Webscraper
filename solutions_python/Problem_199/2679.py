import sys

def flip_all(line):
    return list([not x for x in line])

def flip(row, start, k_size):
    row[start:start + k_size] = flip_all(row[start:start + k_size])


def solve(row, k_size):
    flip_count = 0
    for c in range(0, len(row) - k_size + 1):
        if row[c] == False:
            flip(row, c, k_size)
            flip_count += 1
        # print(row)

    return flip_count if all(row) else "IMPOSSIBLE"

def main():
    f = open(sys.argv[1])
    f_out = open(sys.argv[2], 'w')
    tests = int(f.readline())
    for i in range(0, tests):
        row, k_size = f.readline().split()
        row = [True if x == "+" else False for x in row]
        f_out.write("Case #{}: {}\n".format(i + 1, solve(row, int(k_size))))


if __name__ == "__main__":
    main()