__author__ = 'Lauri Elias'

with open('input.txt') as f:
    content = f.readlines()

out = open('output.txt', 'w')
for case, line in enumerate(content[1:]):
    line_data = line.strip().split(' ')
    shyness_array = list(map(int, list(line_data[1])))
    shyness_threshold = 0
    min_friends = 0
    for shyness, count in enumerate(shyness_array):
        if shyness > shyness_threshold:
            min_friends += shyness - shyness_threshold
            shyness_threshold = shyness
        shyness_threshold += count

    out.write('Case #%d: %s\n' % (case + 1, min_friends))
out.close()