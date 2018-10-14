import sys

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

num_tests = int(src.readline().rstrip())
def draw(table):
    for row in table: print ''.join(row)

for test_idx in range(1,num_tests+1):
    R, C = [int(each) for each in src.readline().split(' ')]
    table = []
    children = []
    for row_number in range(R):
        row = [each for each in src.readline().rstrip()]
        for column_number, each in enumerate(row):
            if not(each=='?'):
                children.append((row_number, column_number))
        table.append(row)
    draw(table)
    print 'Children: ', children
    blanks = R*C - len(children)

    def check_only_one(left_x, right_x, left_y, right_y, letter):
        for dx in range(left_x, right_x+1):
            for dy in range(left_y, right_y+1):
                if not((table[dx][dy]==letter) or (table[dx][dy]=='?')):
                    return False
        return True

    def fill(table, left_x, right_x, left_y, right_y, letter):
        for dx in range(left_x, right_x+1):
            for dy in range(left_y, right_y+1):
                table[dx][dy] = letter

    def clear(table, left_x, right_x, left_y, right_y, letter):
        for dx in range(left_x, right_x+1):
            for dy in range(left_y, right_y+1):
                table[dx][dy] = '?'

    def backgate(table, child, filled_count):
        if child==len(children):
            if filled_count==blanks:
                print '------------------YAY!'
                draw(table)
                print '------------------YAY!'
                return True
            print 'WOOP!'
            return False
        x,y = children[child]
        letter = table[x][y]
        print 'doing letter:', letter
        for left_x in range(0, x+1, 1):
            for right_x in range(R-1, x-1, -1):
                for left_y in range(0, y+1, 1):
                    for right_y in range(C-1, y-1, -1):
                        empty = check_only_one(left_x, right_x, left_y, right_y, letter)
                        if not empty:
                            continue
                        fill(table, left_x, right_x, left_y, right_y, letter)
                        cur_fillings = (right_y +1 - left_y)*(right_x +1 - left_x) - 1
                        # print 'At ', letter, ' with [%s,%s] with %s blanks left' % (x, right_x, blanks - filled_count - cur_fillings)
                        draw(table)
                        if child < len(children):
                            match = backgate(table, child + 1, filled_count + cur_fillings)
                            if match:
                                return match
                        clear(table, left_x, right_x, left_y, right_y, letter)
                        table[x][y] = letter

    backgate(table, 0, 0)
    result.write('Case #%s:\n' % test_idx)
    for row in table:
        result.write(''.join(row))
        result.write('\n')
