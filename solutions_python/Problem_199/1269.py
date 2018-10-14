def remove_trailing_newlines(text):
    while text[-1] == '\n':
        text = text[:-1]
    return text

def flip_all_pancakes(pancakes):
    flipped_pancakes = ''
    for p in pancakes:
        if p == '-':
            flipped_pancakes = flipped_pancakes + '+'
        else:
            flipped_pancakes = flipped_pancakes + '-'
    return flipped_pancakes

def flip_pancakes(pancakes, start, length):
    return pancakes[:start] + flip_all_pancakes(pancakes[start: start + length]) + pancakes[start + length:]

def verify_pancakes(pancakes):
    for p in pancakes:
        if p == '-':
            return False
    return True

def solve_case(line):
    split_line = line.split(' ')
    pancakes = split_line[0]
    flipper_len = int(split_line[1])
    n_flips = 0

    for i in range(0, len(pancakes) - flipper_len + 1):
        if pancakes[i] == '-':
            pancakes = flip_pancakes(pancakes, i, flipper_len)
            n_flips += 1

    print(pancakes)
    if verify_pancakes(pancakes):
        return n_flips

    return 'IMPOSSIBLE'

lines = []
with open('A-large.in') as f:
    text = f.read()
    text = remove_trailing_newlines(text)
    lines = text.split('\n')
    f.close()

lines = lines[1:]
solutions = []

for i in range(len(lines)):
    line = lines[i]
    solution = solve_case(line)
    outline = 'Case #' + str(i + 1) + ': ' + str(solution)
    solutions.append(outline)

with open('A-large.out', 'w') as f:
    for line in solutions:
        f.write(line + '\n')
    f.close()
