import sys
import codejam


def flipped(cakes):
    return list('+' if cake == '-' else '-' for cake in cakes)


def flip_count(cakes, fsize):
    cakes = list(cakes)
    count = 0
    for i in range(len(cakes) - fsize + 1):
        if cakes[i] == '-':
            cakes[i:i+fsize] = flipped(cakes[i:i+fsize])
            count += 1
    if all(cake == '+' for cake in cakes):
        return count
    else:
        return 'IMPOSSIBLE'


def parser(reader):
    cakes, fsize = reader.readline().split()
    return flip_count(cakes, int(fsize))


if __name__ == '__main__':
    codejam.run(parser, open('A-large.in', 'r'), open('pancake-large.out', 'w'))
