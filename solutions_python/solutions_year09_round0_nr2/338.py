#!/usr/bin/python

# THIS IS A VERY UGLY ALGORITHM

def mark(sinks, basins):
    c = 'A'
    for y in range(len(sinks)):
        for x in range(len(sinks[0])):
            if sinks[y][x]:
                sinks[y][x] = c
                c = chr(ord(c) + 1)
            else:
                sinks[y][x] = ''
    done = False
    while not done:
        done = True
        for y in range(len(sinks)):
            for x in range(len(sinks[0])):
                if sinks[y][x] != '':
                    for neighbors in basins[y][x]:
                        if sinks[neighbors[0]][neighbors[1]] == '':
                            sinks[neighbors[0]][neighbors[1]] = sinks[y][x]
                            done = False


def link(alts):
    basins = []
    sinks = []
    for y in range(len(alts)):
        basins.append([])
        sinks.append([])
        for x in range(len(alts[0])):
            basins[y].append([])
            sinks[y].append(False)

    for y in range(len(alts)):
        for x in range(len(alts[0])):
            deepest = alts[y][x]
            if y - 1 >= 0:
                if alts[y - 1][x] < deepest:
                    deepest = alts[y - 1][x]
                    x_ = x
                    y_ = y - 1
            if x - 1 >= 0:
                if alts[y][x - 1] < deepest:
                    deepest = alts[y][x - 1]
                    x_ = x - 1
                    y_ = y
            if x + 1 < W:
                if alts[y][x + 1] < deepest:
                    deepest = alts[y][x + 1]
                    x_ = x + 1
                    y_ = y
            if y + 1 < H:
                if alts[y + 1][x] < deepest:
                    deepest = alts[y + 1][x]
                    x_ = x
                    y_ = y + 1
            if deepest < alts[y][x]:
                basins[y_][x_].append((y, x))
            else:
                sinks[y][x] = True

    return (basins, sinks)

def replace_chars(sinks):
    c = 'a'
    assoc = dict()
    for y in range(len(sinks)):
        for x in range(len(sinks[0])):
            if assoc.has_key(sinks[y][x]):
                sinks[y][x] = assoc[sinks[y][x]]
            else:
                assoc[sinks[y][x]] = c
                sinks[y][x] = c
                c = chr(ord(c) + 1)


input_file = open('B-large.in')
output_file = open('output', 'w')

T = int(input_file.readline())


for t in range(T):
    (H, W) = map(int, input_file.readline().split(' '))
    alts = []
    for h in range(H):
        alts.append(map(int, input_file.readline().split(' ')))

    basins, sinks = link(alts)

    mark(sinks, basins)

    replace_chars(sinks)

    output_file.write("Case #" + str(t + 1) + ":\n")
    for line in sinks:
       output_file.write(' '.join(line) + "\n")

input_file.close()
output_file.close()
