def main(line):
    n, k = line.split()
    n = int(n)
    k = int(k)

    choices = {}
    keys = []
    stalls = [n]
    for k_idx in range(k):
        max_stall = max(stalls) - 1
        left = max_stall // 2
        right = max_stall - left
        max_idx = stalls.index(max_stall + 1)
        stalls[max_idx] = left
        stalls.insert(max_idx + 1, right)
    return "{} {}".format(max(left, right), min(left, right))


if __name__ == '__main__':
    with open('C-small.out', 'w') as outfile:
        with open('C-small.in', 'r') as file:
            count = int(file.readline())
            for idx in range(1, count + 1):
                line = file.readline()
                outfile.write("Case #{}: {}\n".format(idx, main(line)))


            