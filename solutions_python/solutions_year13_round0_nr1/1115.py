import sys

VALUES = {'X':1, 'O':10, 'T':11, '.':100}

def get_line_winner(line):
    line_str = str(line)
    if line_str[-1] == '4': return 'X'
    elif line_str[-2] == '4': return 'O'
    else: return None


def find_game_status(grid):
    column_counts = [0, 0, 0, 0]
    diagonal_counts = [0, 0]
    draw = True  # for now

    for row_index, row in enumerate(grid):
        row_count = 0;
        for column_index, square in enumerate(row):
            square_value = VALUES[square]
            row_count += square_value
            column_counts[column_index] += square_value
            if row_index == column_index: diagonal_counts[0] += square_value
            if (row_index) == (3 - column_index): diagonal_counts[1] += square_value
        row_winner = get_line_winner(row_count)
        if row_winner is not None: return str(row_winner) + ' won'
        if row_count >= 100: draw = False  # there's at least one '.'
    for column in column_counts:
        column_winner = get_line_winner(column)
        if column_winner is not None: return str(column_winner) + ' won'
    for diagonal in diagonal_counts:
        diagonal_winner = get_line_winner(diagonal)
        if diagonal_winner is not None: return str(diagonal_winner) + ' won'
    return 'Draw' if draw else 'Game has not completed'


def main(input_file_name, output_file_name):
    input_file = open(input_file_name, 'rU')
    output_file = open(output_file_name, 'w')
    for case in range(int(input_file.readline())):
        grid = []
        for row in range(4): grid.append(input_file.readline().splitlines()[0])
        game_status = find_game_status(grid)
        output_file.write('Case #' + str(case+1) + ': ' + game_status + '\n')
        input_file.readline()  # blank line separating each grid, present after last grid too
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
