def count_steps(row, flipper_width):
    steps = 0
    pos = 0

    while not all(row):
        while row[pos] == 1:
            pos += 1
            if pos + flipper_width > len(row):
                return None

        for i in range(flipper_width):
            row[pos + i] = 0 if row[pos + i] else 1

        steps += 1

    return steps

def bytearray_row(row):
    return bytearray(0 if c == '-' else 1 for c in row)

if __name__ == "__main__":
    tests_count = int(input())

    for i in range(1, tests_count+1):
        row, flipper_width = input().split()
        steps = count_steps(bytearray_row(row), int(flipper_width))
        print('Case #{}: {}'.format(i, steps if steps is not None else 'IMPOSSIBLE'))
