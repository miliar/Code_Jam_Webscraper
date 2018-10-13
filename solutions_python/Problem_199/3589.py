from sys import argv


def flip_pancakes(pancakes, K, last_unhappy):
    new_stack = pancakes[:last_unhappy - K + 1]
    if isinstance(new_stack, str):
        new_stack = [new_stack]
    p = {'+': '-', '-': '+'}
    flipped = [p[i] for i in pancakes[last_unhappy - K + 1:last_unhappy + 1]]
    last = pancakes[last_unhappy + 1:]
    if isinstance(last, str):
        last = [last]
    return "".join(new_stack + flipped + last)


def find_number_of_flips(data):
    K = int(data.split()[1])
    pancakes = data.split()[0]
    stack_size = len(pancakes)
    flips = 0
    while '-' in pancakes:
        last_unhappy = stack_size - pancakes[::-1].index('-') - 1
        if last_unhappy - K >= -1:
            pancakes = flip_pancakes(pancakes, K, last_unhappy)
            flips += 1
        else:
            return 'IMPOSSIBLE'
    return flips


infile = argv[1]
with open(infile) as a:
    testcases = a.read().splitlines()[1:]

for i, case in enumerate(testcases):
    flips = find_number_of_flips(case)
    print "Case #{}: {}".format(i + 1, flips)
