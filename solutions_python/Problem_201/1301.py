import math

def the_value_or_zero(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return 0

def solve_case(line):
    split_line = line.split(' ')
    stalls = int(split_line[0])
    remaining_people = int(split_line[1])
    gaps = [stalls]
    gap_counts = {stalls:1}
    while remaining_people > 1:
        gap = gaps[0]
        pops = min(remaining_people - 1, gap_counts[gap])
        remaining_people -= pops
        gap_counts[gap] = gap_counts[gap] - pops

        if (gap > 1):
            gap = (gap - 1) / 2
            big = math.ceil(gap)
            small = math.floor(gap)
            if big == small:
                if big in gap_counts:
                    gap_counts[big] = gap_counts[big] + 2 * pops
                else:
                    gap_counts[big] = 2 * pops
                    gaps = gaps + [big]
            else:
                if big in gap_counts:
                    gap_counts[big] = gap_counts[big] + pops
                else:
                    gap_counts[big] = pops
                    gaps = gaps + [big]
                if small in gap_counts:
                    gap_counts[small] = gap_counts[small] + pops
                else:
                    gap_counts[small] = pops
                    gaps = gaps + [small]

        if gap_counts[gaps[0]] == 0:
            gaps = gaps[1:]

    gap = gaps[0]
    gap = (gap - 1) / 2
    return str(math.ceil(gap)) + ' ' + str(math.floor(gap))

def remove_trailing_newlines(text):
    while text[-1] == '\n':
        text = text[:-1]
    return text

FILENAME = 'C-small-2-attempt0'
lines = []
with open(FILENAME + '.in') as f:
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

with open(FILENAME + '.out', 'w') as f:
    for line in solutions:
        print(line)
        f.write(line + '\n')
    f.close()
