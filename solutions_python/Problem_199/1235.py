def flip(pancakes, flipper_length, index):
    if flipper_length + index > len(pancakes):
        return pancakes

    flipped = pancakes
    for i in xrange(flipper_length):
        flipped[index + i] = '+' if flipped[index + i] == '-' else '-'

    return flipped

def solve(pancakes, flipper_length):
    solution = 0
    for i in xrange(len(pancakes)):
        if pancakes[i] == '-':
            pancakes = flip(pancakes, flipper_length, i)
            solution += 1

    if any(pancake == '-' for pancake in pancakes):
        return 'IMPOSSIBLE'
    return solution

if __name__ == '__main__':
    lines = open('A-large.in', 'r').readlines()
    test_cases = int(lines[0])
    for i in xrange(1, len(lines)):
        pancakes, flipper_length = lines[i].split()

        print 'Case #{0}: {1}'.format(i, solve(list(pancakes), int(flipper_length)))