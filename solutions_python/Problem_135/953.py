import sys

f = open(sys.argv[1], 'r')

line = f.readline()
line = f.readline()

case = 1
while line:
    usr_row = int(line)

    for i in xrange(1, 5):
        if i == usr_row:
            row = set(f.readline().split())
        else:
            f.readline()

    usr_row2 = int(f.readline())

    for i in xrange(1, 5):
        if i == usr_row2:
            row2 = set(f.readline().split())
        else:
            f.readline()

    inter = row & row2

    result = 'Bad magician!'

    if not inter:
        result = 'Volunteer cheated!'
    elif len(inter) == 1:
        result = list(inter)[0]

    print 'Case #%d: %s' % (case, result)

    line = f.readline()
    case += 1