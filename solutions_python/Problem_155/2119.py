import sys

def compute(Smax, S):
    people_up = 0
    add_people = 0
    for val in S:
        people_up += val
        people_up -= 1
        if -1 == people_up:
            add_people += 1
            people_up = 0

    return add_people

def make_output(SList):
    output_lines = []
    for index, element in enumerate(SList):
        val = compute(element[0], element[1])
        output_lines.append('Case #%d: %d\n' % (index + 1, val))

    return output_lines

def parse(input_file):
    f = open(input_file)
    T = int(f.readline())
    SList = []

    for index in range(T):
        Smax, S = f.readline().split(' ')
        Smax = int(Smax)
        S = [int(i) for i in S.strip()]
        if Smax + 1 != len(S):
            raise ValueError
        SList.append([Smax, S])

    f.close()
    return SList

def write_file(input_file, output_lines):
    output_file = input_file[:-2] + 'out'
    f = open(output_file, 'w')
    f.writelines(output_lines)
    f.close()

if '__main__' == __name__:
    write_file(sys.argv[1], make_output(parse(sys.argv[1])))
