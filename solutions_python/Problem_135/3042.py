import math

def prep_file(fileName):
    f = open(fileName, 'r');
    return f.readlines();

def solve_case(lines):
    m = 'Bad magician!'
    v = 'Volunteer cheated!'

    l1 = int(lines[0].replace('\n', ''))
    l2 = int(lines[5].replace('\n', ''))

    #print l1, l2, len(lines)

    line1 = set(lines[l1].replace('\n', '').split(' '))
    line2 = set(lines[l2+5].replace('\n', '').split(' '))
    res = compareLines(line1, line2)
    print res

    if len(res) > 1:
        return m
    elif len(res) == 1:
        return res[0]
    else:
        return v

def compareLines(line1, line2):
    matches = []
    for l in line1:
        if l in line2:
            matches.append(l)
    return matches


def main(fileName, outputName):

    f = prep_file(fileName)
    cases = f.pop(0)

    output = ''
    counter = 1

    for i in range(0, int(cases) * 10, 10):
	r = solve_case(f[i:i+10])
        output = output + 'Case #' + str(counter) + ': ' + str(r) + '\n';
	counter = counter + 1
    f = open(outputName, 'w+');
    f.write(output[:-1]);

main("attempt1.in", "output1.txt")
