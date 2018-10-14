def parse_line(line):
    sp = line.split(" ")
    max_shy = int(sp[0])
    sp_levels = list(sp[1][:-1])
    levels = [int(s) for s in sp_levels]
    return max_shy, levels


def find_holes(max_shy, levels):
    level_range = range(len(levels))
    hole = 0
    standing = 0
    for i in level_range:
        if levels[i] == 0:
            continue
        if standing >= i:
            standing += levels[i]
        else:
            hole = hole + (i-standing)
            standing = standing + hole + levels[i]
    return hole


def standing_ovation(filename):
    fin = open(filename, 'r')
    out = open('standing_ovation.out', 'w')
    cases = int(fin.readline())
    case = 1
    while case <= cases:
        line = fin.readline()
        max_shy, levels = parse_line(line)
        hole = find_holes(max_shy, levels)
        out.write('Case #%d: %d\n' % (case, hole))

        case +=1

    fin.close()
    out.close()

standing_ovation('A-small-attempt0.in')