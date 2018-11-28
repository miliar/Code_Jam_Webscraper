from math import floor, ceil

def min_time(plates):
    print('START', plates)
    splits = [0]*len(plates)
    best_time = time(plates, splits)
    for improved_time in optimize(plates, splits):
        if improved_time > best_time:
            break
        best_time = improved_time
    return best_time

def optimize(plates, splits):
    while max(eat_time(plates, splits)) > 1:
        max_pancakes = max(eat_time(plates, splits))
        for plate, pancakes in enumerate(plates):
            if plate_time(pancakes, splits[plate]) == max_pancakes:
                splits[plate] += 1
        yield time(plates, splits)

def time(plates, splits):
    return max(eat_time(plates, splits)) + sum(splits)

def eat_time(plates, splits):
    table = list(zip(plates, splits))
    return [plate_time(pancake, split) for pancake, split in table]

def plate_time(pancakes, split):
    return ceil(pancakes/(split+1.0))

filename = 'B-small-attempt2'
output = ''
with open(filename+'.in', 'r') as file:
    case_num = 0
    _ = file.readline()  # Number of cases
    line = file.readline()  # Number of plates with pancakes
    while line is not '':
        case_num += 1
        txt = file.readline().strip('\n').split(' ')
        plates = list(map(int, txt))
        output += 'Case #{}: {}\n'.format(case_num, min_time(plates))
        line = file.readline()

with open(filename+'.out', 'w') as file:
    file.write(output)