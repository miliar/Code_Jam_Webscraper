INPUT_FILE = __file__.replace('.py', '.input')
OUTPUT_FILE = __file__.replace('.py', '.output')


def flip(pancakes, i, k):
    for j in range(i, i+k):
        pancakes[j] = not pancakes[j]
    return pancakes


def solve(pancakes, k):
    mapping = {
        '-': False,
        '+': True
    }
    pancakes = [mapping[p] for p in pancakes]

    count = 0

    for i in range(len(pancakes) - k + 1):
        if not pancakes[i]:
            pancakes = flip(pancakes, i, k)
            count += 1

    if all(pancakes):
        return count
    else:
        return "IMPOSSIBLE"


def main():

    with open(INPUT_FILE, 'r') as f, open(OUTPUT_FILE, 'w') as g:
        for i, line in enumerate(f):
            if i == 0:
                continue
            pancakes, k = line.strip().split()
            k = int(k)
            outline = 'Case #{i}: {soln}\n'.format(i=i, soln=solve(pancakes, k))
            g.write(outline)
            print outline,


if __name__ == '__main__':
    main()
