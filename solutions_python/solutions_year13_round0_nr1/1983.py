import sys

T = int(sys.stdin.readline())

def readInput():
    field = []
    for i in xrange(4):
        field.append(list(sys.stdin.readline().rstrip()))
    return field

def check_winner(line):
    if line.count('O') == 4 or (line.count('O') == 3 and 'T' in line):
        return 'O won'
    elif line.count('X') == 4 or (line.count('X') == 3 and 'T' in line):
        return 'X won'
    else:
        return None

def check_field(field):
    # holizon
    for way in [field,
            zip(*field),
            [[field[i][i] for i in xrange(4)]],
            [[field[i][3-i] for i in xrange(4)]]]:
        for i in way:
            result = check_winner(i)
            if result != None:
                return result
    for line in field:
        if '.' in line:
            return 'Game has not completed'
    return 'Draw'

if __name__ == "__main__":
    for i in xrange(T):
        field = readInput()
        print "Case #{0}: {1}".format(i+1, check_field(field))
        sys.stdin.readline()
