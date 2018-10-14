import sys


#################################
# Helpers


def characters_to_grid(lines):
    """
    Convert an input grid of strings to the grid, also outputting the kid identifiers and starting positions
    """
    kids = []
    grid = []
    for i, line in enumerate(lines):
        grid.append([])
        for j, char in enumerate(line):
            if char != '?':
                # Each 'kid' is a tuple (startx, starty, identifier)
                kids.append((j, i, ord(char) - ord('A')))
            grid[-1].append(-1 if char == '?' else ord(char) - ord('A'))

    return grid, kids


def grid_to_characters(grid):
    """
    Convert a grid to the output characters
    """
    chars = []
    for row in grid:
        cur_row = []
        for cell in row:
            cur_row.append('?' if cell == -1 else chr(cell + ord('A')))
        chars.append(''.join(cur_row))
    return chars


#################################
# Solution


def clone_grid(grid):
    """
    Create a deep copy of a grid
    """
    return [[cell for cell in row] for row in grid]


def is_extent_free(grid, start, x_extent, y_extent, id):
    """

    :param grid: the grid to check
    :param start: the x and y position to start from (x, y)
    :param x_extent: the x extent (x_left, x_right)
    :param y_extent: the y extent (y_top, y_bottom)
    :param id: the id being checked for (i.e. this id's spaces will be considered free)
    :return: True iff no id other than the one provided controls squares in the rectangle
             and the rectangle is within grid bounds
    """
    x, y = start
    x_left, x_right = x_extent
    y_top, y_bottom = y_extent

    x_min = x - x_left
    x_max = x + x_right + 1
    y_min = y - y_top
    y_max = y + y_bottom + 1

    # Check bounds
    if x_min < 0 or x_max > len(grid[0]):
        return False
    if y_min < 0 or y_max > len(grid):
        return False

    # get the subgrid defined by the rectangle
    subgrid = [row[x_min:x_max] for row in grid[y_min:y_max]]

    potato = 5

    # Check if there are kids other than the id in there
    for row in subgrid:
        for cell in row:
            if cell != -1 and cell != id:
                return False

    return True


def allocate_kid(grid, kid):
    """
    Allocate one kid space on the grid

    :param grid: the grid
    :param kid: the kid tuple (xstart, ystart, identifier)
    :return: a cloned and allocated grid
    """
    # Clone the grid
    grid = clone_grid(grid)
    x_start, y_start, id = kid

    # Need to decide the x and y extents this kid is allocated
    # Initialise at 1x1 (their initial slice)
    x_left = 0
    x_right = 0
    y_top = 0
    y_bottom = 0

    # Determine x extent first
    # Extend left
    while is_extent_free(grid, (x_start, y_start), (x_left + 1, x_right), (y_top, y_bottom), id):
        x_left += 1
    # Extend right
    while is_extent_free(grid, (x_start, y_start), (x_left, x_right + 1), (y_top, y_bottom), id):
        x_right += 1

    # Determine y extent
    # Extend up
    while is_extent_free(grid, (x_start, y_start), (x_left, x_right), (y_top + 1, y_bottom), id):
        y_top += 1
    # Extend down
    while is_extent_free(grid, (x_start, y_start), (x_left, x_right), (y_top, y_bottom + 1), id):
        y_bottom += 1

    # Allocate the grid space found to be available
    for y in range(y_start - y_top, y_start + y_bottom + 1):
        for x in range(x_start - x_left, x_start + x_right + 1):
            grid[y][x] = id

    return grid


def solve(grid, kids):
    for kid in kids:
        grid = allocate_kid(grid, kid)

    return grid


#################################
# Parse input


def run():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    results = []
    with open(input_file, 'r') as f:
        num_cases = int(f.readline())

        # Parse each test case
        for i in range(0, num_cases):
            first_line = f.readline()
            R = int(first_line.split(' ')[0])
            C = int(first_line.split(' ')[1])
            lines = [f.readline().strip() for j in range(0, R)]

            (grid, kids) = characters_to_grid(lines)

            answer = grid_to_characters(solve(grid, kids))

            results.append('Case #{0}:\n'.format((i + 1)))
            for line in answer:
                results.append("{0}\n".format(line))
            print('Solved {0}/{1}'.format((i + 1), num_cases))

    with open(output_file, 'w') as f:
        f.writelines(results)

    print('[Complete]')

if __name__ == '__main__':
    run()
