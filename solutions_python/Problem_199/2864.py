

def flip(pancakes, at, k):
    to_flip = pancakes[at:at+k]
    assert len(to_flip) == k
    return pancakes[:at] + to_flip.translate(str.maketrans('+-', '-+')) + pancakes[at+k:]


def solve(pancakes, k):
    k = int(k)
    flip_count = 0
    for i in range(len(pancakes[:-k]) + 1):
        if pancakes[i] == '-':
            pancakes = flip(pancakes, i, k)
            flip_count += 1
    if all(c == '+' for c in pancakes):
        return str(flip_count)
    else:
        return 'IMPOSSIBLE'


solutions = []
with open('A-large.in', 'r') as input_file:
    input_file.readline()
    for line in input_file:
        solutions.append(solve(*line.split()))

with open('A-large.out', 'w') as output_file:
    for line in (f'Case #{i}: ' + solution for i, solution in enumerate(solutions, start=1)):
        output_file.write(line + '\n')
