FILENAME = 'A-large.in'

with open(FILENAME, 'r') as f:
    lines = f.read().splitlines()

num_test_cases = int(lines[0])

for i in xrange(1, num_test_cases + 1):
    line = lines[i].split(' ')
    max_shyness = int(line[0])
    counts = [int(member) for member in line[1]]
    running_total = [counts[0]]

    for j in counts[1:]:
        running_total.append(running_total[-1] + j)

    result = 0
    for index, count in enumerate(running_total):
        if count + result <= index:
            result += index - (count + result) + 1

    print 'Case #' + str(i) + ': ' + str(result)
