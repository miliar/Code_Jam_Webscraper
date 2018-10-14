def flip_pancake(pancake):
    if pancake == '+':
        return '-'
    elif pancake == '-':
        return '+'
    else:
        print 'THERE IS AN ERROR'

input_file = open('pancake_flipper.in')
out_file = open('pancake_flipper.out', 'w')
out_file.truncate()

lines = []
for line in input_file:
    lines.append(line.rstrip())
num_cases = int(lines[0])
for i in xrange(num_cases):
    line = lines[i + 1]
    arr = line.split(' ')
    pancakes = list(arr[0])
    flipper_size = int(arr[1])
    # print pancakes
    # print flipper_size
    num_flips = 0
    positions = []
    for j in xrange(len(pancakes) - flipper_size + 1):
        if pancakes[j] == '-':
            num_flips += 1
            positions.append(j)
            for k in xrange(flipper_size):
                pancakes[j+k] = flip_pancake(pancakes[j+k])
    for j in xrange(flipper_size):
        if pancakes[len(pancakes) - flipper_size + j] != '+':
            num_flips = -1
            break
    if num_flips >= 0:
        # print num_flips
        # print positions
        out_file.write('Case #{}: {}\n'.format(i + 1, num_flips))
    else:
        # print 'POSSIMPIBLE'
        out_file.write('Case #{}: {}\n'.format(i + 1, 'IMPOSSIBLE'))
