pancakes = list("-+-+-")


def flip(pancakes, size, index):
    return pancakes[:index] + ['-' if p[0] == '+' else '+' for p in pancakes[index:index + size]] + pancakes[index + size:]


def flipping(pancakes, size):
    flipped = 0
    while True:
        if '-' not in pancakes:
            break
        i = pancakes.index('-')
        if len(pancakes) - i < size:
            break
        new_pancakes = flip(pancakes, size, i)
        flipped += 1
        if pancakes == new_pancakes:
            break
        pancakes = new_pancakes

    if '-' in pancakes:
        return False
    return flipped


fr = open('A-small.in', 'r')
fw = open('A-small.out.txt', 'w+')
numcases = int(fr.readline())
idline = 0

for x in range(1, numcases + 1):
    idline += 1
    inputs = fr.readline().replace('\n', '').split(' ')
    line = flipping(list(inputs[0]), int(inputs[1]))
    if line is False:
        fw.write("Case #" + str(idline) + ": " + 'IMPOSSIBLE' + '\n')
    else:
        fw.write("Case #" + str(idline) + ": " + str(line) + '\n')
