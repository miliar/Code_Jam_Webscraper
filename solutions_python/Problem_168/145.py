import sys

NO_ARROW = '.'
UP_ARROW = '^'
RIGHT_ARROW = '>'
LEFT_ARROW = '<'
DOWN_ARROW = 'v'

def run_test(case_number, generator):
    r, c = [int(x) for x in next(generator).split()]
    level = []
    for row in range(r):
        level.append([x for x in next(generator).strip()])
    arrows = []
    for row in range(r):
        for column in range(c):
            if level[row][column] != NO_ARROW:
                arrows.append((row, column))

    leaving_the_map = []
    for row, column in arrows:
        arrow = level[row][column]
        delta_x = 0
        delta_y = 0
        if arrow == UP_ARROW:
            delta_y = -1
        elif arrow == LEFT_ARROW:
            delta_x = -1
        elif arrow == RIGHT_ARROW:
            delta_x = 1
        elif arrow == DOWN_ARROW:
            delta_y = 1

        check_row = row + delta_y
        check_column = column + delta_x
        left = True
        while 0 <= check_row < r and 0 <= check_column < c:
            if level[check_row][check_column] != NO_ARROW:
                left = False
                break
            check_row += delta_y
            check_column += delta_x

        if left:
            leaving_the_map.append((row, column))

    possible = True
    for (row, column) in leaving_the_map:
        possible_arrows = 0
        for c_row in range(r):
            if level[c_row][column] != NO_ARROW:
                possible_arrows += 1
        for c_column in range(c):
            if level[row][c_column] != NO_ARROW:
                possible_arrows += 1
        if possible_arrows <= 2:
            possible = False
            break
    if possible:    
        print('Case #%d: %d' % (case_number, len(leaving_the_map)))
    else: 
        print('Case #%d: IMPOSSIBLE' % (case_number))

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()