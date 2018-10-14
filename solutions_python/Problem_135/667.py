
def process_file(file):
    fsock = open(file)
    text = fsock.read()
    fsock.close()
    lines = text.split('\n')
    return lines

def process_lines(lines):
    cases = []
    n = int(lines[0].split(' ')[0])
    i = 1
    while len(cases) < n:
        answer1 = int(lines[i])
        i += answer1
        v1 = set(lines[i].split())
        i += (5-answer1)

        answer2 = int(lines[i])
        i += answer2
        v2 = set(lines[i].split())
        i += (5-answer2)

        cases.append(v1 & v2)
    return cases

def process_case(case):
    if len(case) == 0:
        return "Volunteer cheated!"
    elif len(case) == 1:
        return case.pop()
    else:
        return "Bad magician!"

def main():
    import sys
    if len(sys.argv) == 1:
        filename = 'x.in'
    else:
        filename = sys.argv[1]
    lines = process_file(filename)
    cases = process_lines(lines)
    for k, v in enumerate(cases):
        case = process_case(v)
        if type(case) != type(()):
            print "Case #%d: %s" % (k + 1, case)
        else:
            print "Case #%d: %s %s" % (k + 1, case[0], case[1])

if __name__ == "__main__":
    main()