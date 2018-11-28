import re
def pancake(filename):
    with open(filename, 'r') as f:
        numTests = f.readline()
        output = open('pancake_out.txt', 'w')
        for idx in range(1, int(numTests)+1):
            line = re.split(' ', f.readline())
            pancakes = list(line[0])
            k = int(line[-1][:-1])

            flips = 0

            for i in range(len(pancakes)-k):
                if pancakes[i] == '-':
                    for j in range(k):
                        flip(pancakes, i+j)
                    flips += 1

            if len(set(pancakes[-k:])) == 1:
                if pancakes[-k] == '+':
                    pass
                elif flips != 0:
                    flips += 1
                elif pancakes[-k] == '-':
                    flips += 1
            else:
                flips = 'IMPOSSIBLE'

            output.write('Case #%d: %s\n' % (idx, str(flips)))

def flip(pancakes, i):
    if pancakes[i] == '+':
        pancakes[i] = '-'
    else:
        pancakes[i] = '+'

pancake('A-large.in.txt')
