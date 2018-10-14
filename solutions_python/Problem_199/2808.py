def process(file_name):
    with open(file_name) as f:
        input = f.readlines()[1:]
    for i, line in enumerate(input):
        line_list = line.split(' ')
        ans = pancake(line_list[0], int(line_list[1]))
        print 'Case #%s: %s' % (i + 1, ans)

def pancake(cake_str, k):
    count = 0

    cakes = list(cake_str)

    for i in range(len(cakes) - k + 1):
        if cakes[i] == '+':
            continue
        cakes[i:i + k] = flip(cakes[i:i + k])
        count += 1

    for cake in cakes[-k:]:
        if cake == '-':
            return "IMPOSSIBLE"

    return count


def flip(cakes):
    res = []
    for cake in cakes:
        if cake == '+':
            res.append('-')
        else:
            res.append('+')
    return res


if __name__ == '__main__':
    process("test_input.txt")
