def get_row():
    return int(input())
    
def get_grid():
    return [input().split() for row in range(GRID_SIZE)]

if __name__ == '__main__':
    GRID_SIZE = 4

    lines = open('A-small-attempt0.in')
    input = lines.readline
    
    cases = int(input())

    for case in range(cases):
        row_num = get_row()
        grid = get_grid()
        grid_row1 = set(grid[row_num-1])
        
        row_num = get_row()
        grid = get_grid()
        grid_row2 = set(grid[row_num-1])

        cards = grid_row1.intersection(grid_row2)
        
        if len(cards) == 1:
            answer = cards.pop()
        elif len(cards) > 1:
            answer = "Bad magician!"
        else:
            answer = "Volunteer cheated!"

        print("Case #{}: {}".format(case+1, answer))
