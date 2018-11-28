import math

def solve_case(destination, horses):
    time = 0
    for horse in horses:
        pos, speed = [int(x) for x in horse.split(' ')]
        t = (destination - pos) / speed
        time = max(time, t)
    return destination / time

def remove_trailing_newlines(text):
    while text[-1] == '\n':
        text = text[:-1]
    return text

FILENAME = 'A-large'
lines = []
with open(FILENAME + '.in') as f:
    text = f.read()
    text = remove_trailing_newlines(text)
    lines = text.split('\n')
    f.close()

ntests = int(lines[0])
lines = lines[1:]
solutions = []
index = 0

for i in range(ntests):
    dims = lines[index]
    destination, nhorses = [int(x) for x in dims.split(' ')]
    horses = lines[index+1:index+1+nhorses]
    index += nhorses + 1
    solution = solve_case(destination, horses)
    outline = 'Case #' + str(i + 1) + ': ' + str(solution)
    solutions.append(outline)

with open(FILENAME + '.out', 'w') as f:
    for line in solutions:
        print(line)
        f.write(line + '\n')
    f.close()
