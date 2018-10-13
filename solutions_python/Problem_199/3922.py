def run(file):
    with open(file) as f, open('output.txt', 'w') as ff:
        header = f.readline().strip()
        content = f.readlines()
        content = [x.strip() for x in content]
        row = 1

        for c in content:
            count = 0
            ff.write('Case #' + str(row) + ': ' + str(flip(c, count))+'\n')
            row += 1


def flip(line, count):
    blankFlag = line.find('-')
    happyFlag = line.find('+')
    line = line.split()
    pancakesPerRow = int(line[1])
    line = line[0]

    if blankFlag < 0:  # all happy faces
        return count
    elif happyFlag < 0:  # all blank
        if len(line) % pancakesPerRow == 0:
            return len(line) / pancakesPerRow
        else:
            return 'IMPOSSIBLE'
    else:
        index = line.find('-')
        if index > -1 and index+pancakesPerRow <= len(line):
            count += 1
            lit = ''
            for i in range(pancakesPerRow):
                lit += '+' if line[index+i] == '-' else '-'
            line = line[:index]+lit+line[index+pancakesPerRow:]+' '+str(pancakesPerRow)
            print line
            count = flip(line, count)
        else:
            return 'IMPOSSIBLE'
    return count


run('A-small-attempt3.in')