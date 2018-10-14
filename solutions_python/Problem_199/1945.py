import os


def get_next_sad_face(pancakes):
    for i in xrange(0, len(pancakes)):
        if pancakes[i] == '-':
            return i
    return -1


def flip(pancakes, index, count):
    new_pancakes = pancakes[0:index]
    for i in xrange(index, index + count):
        if pancakes[i] == '+':
            new_pancakes = new_pancakes + '-'
        else:
            new_pancakes = new_pancakes + '+'
    new_pancakes = new_pancakes + pancakes[index + count:]
    return new_pancakes


def flip_all(pancakes, count):
    count = int(count)
    flips = 0
    while True:
        index = get_next_sad_face(pancakes)
        if index == -1:
            return flips

        if index > len(pancakes) - count:
            return -1

        pancakes = flip(pancakes, index, count)
        flips += 1

with open('input.txt') as input_file:
    testCases = input_file.readlines()
numTestCases = testCases[0]
testCases.remove(numTestCases)
output_filename = 'output.txt'
if os.path.exists(output_filename):
    os.remove(output_filename)

progress = []
for i in range(0, len(testCases)):
    x = testCases[i].split()
    pancakes = x[0]
    count = x[1]
    progress.append(flip_all(pancakes, count))

with open(output_filename, 'a') as output_file:
    for i in xrange(0, len(progress)):
        if progress[i] == -1:
            to_print = "IMPOSSIBLE"
        else:
            to_print = str(progress[i])
        output_file.write('Case #' + str(i + 1) + ': ' +
                          to_print + '\n')
