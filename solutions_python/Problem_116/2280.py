board = {}
possible4s = (('11','12','13','14'), ('21','22','23','24'), ('31','32','33','34'),
            ('41','42','43','44'), ('11','21','31','41'), ('12','22','32','42'),
            ('13','23','33','43'), ('14','24','34','44'), ('11','22','33','44'), ('14','23','32','41'))

for letter in '1234':
    for number in '1234':
        board[letter + number] = 0
board['T'] = 0

T = 0
originalT = 0
empty = False

def main():
    global T
    global empty
    global originalT
    f = open('A-large.in', 'r')
    o = open('outputLarge.out', 'w')
    lineCount = 1
    T = int(f.readline())
    originalT = T
    for line in f:
        section = lineCount % 5
        if section >= 1:
            for col in xrange(4):
                if line[col] == 'X':
                    board[str(col+1)+str(section)] = 1
                elif line[col] == 'O':
                    board[str(col+1)+str(section)] = -1
                elif line[col] == 'T':
                    board['T'] = str(col+1)+str(section)
                elif line[col] == '.':
                    empty = True
            if T == 1 and section == 4:
                o.write(process(T, empty, originalT))
                for key in board:
                    board[key] = 0
                T -= 1
                empty = False
                break
        else:
            o.write(process(T, empty, originalT) + '\n')
            for key in board:
                board[key] = 0
            T -= 1
            empty = False
        lineCount += 1
    f.close()
    o.close()

def process(T, empty, originalT):
    T = abs(T - originalT) + 1
    for possible4 in possible4s:
        num = sum([board[square] for square in possible4])
        if num == 4:
            return 'Case #' + str(T) + ': X won'
        elif num == -4:
            return 'Case #' + str(T) + ': O won'
        elif num == 3:
            if board['T'] in possible4:
                return 'Case #' + str(T) + ': X won'
        elif num == -3:
            if board['T'] in possible4:
                return 'Case #' + str(T) + ': O won'
    if empty:
        return 'Case #' + str(T) + ': Game has not completed'
    return 'Case #' + str(T) + ': Draw'

main()
