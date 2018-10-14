input_file = open('tidy_numbers.in')
out_file = open('tidy_numbers.out', 'w')
out_file.truncate()

lines = []
for line in input_file:
    lines.append(line.rstrip())
num_cases = int(lines[0])
for i in xrange(num_cases):
    line = lines[i + 1]
    numbers = list(line)
    found_break = False
    for j in xrange(len(numbers) - 1):
        if not found_break:
            if int(numbers[j]) > int(numbers[j+1]):
                found_break = True
                numbers[j] = str(int(numbers[j]) - 1)
                for k in reversed(xrange(j)):
                    if int(numbers[k+1]) < int(numbers[k]):
                        numbers[k+1] = '9'
                        numbers[k] = str(int(numbers[k]) - 1)
                numbers[j+1] = '9'
        else:
            numbers[j+1] = '9'
    # print ''.join(numbers).lstrip('0')
    out_file.write('Case #{}: {}\n'.format(i + 1, ''.join(numbers).lstrip('0')))
