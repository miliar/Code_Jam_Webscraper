import sys

def read_single_row(f):
    return set(int(item) for item in f.next().strip().split())

def get_row(answer, f):
    rows = [
        read_single_row(f) for i in range(4)
    ]
    return rows[answer - 1]

def read_sample(path):
    f = open(path)
    number_of_cases = int(f.next())
    for i in range(number_of_cases):
        case = i + 1

        answer1 = int(f.next())
        row1 = get_row(answer1, f)
        answer2 = int(f.next())
        row2 = get_row(answer2, f)

        possibilities = row1.intersection(row2)

        if len(possibilities) == 0:
            print 'Case #%d: Volunteer cheated!' % case
        elif len(possibilities) == 1:
            print 'Case #%d: %d' % (case, possibilities.pop())
        else:
            print 'Case #%d: Bad magician!' % case

if __name__ == '__main__':
    read_sample(sys.argv[-1])
