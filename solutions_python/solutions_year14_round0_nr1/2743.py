def get_line():
    return raw_input().strip("\n")

def determine_card(row1, grid1, row2, grid2):
    possible_cards = grid1[row1]
    return [card for card in grid2[row2] if card in possible_cards]


num_cases = int(get_line())
for case in xrange(1, num_cases + 1):
    first_row = int(get_line())
    first_grid = [
        map(int, get_line().split()),
        map(int, get_line().split()),
        map(int, get_line().split()),
        map(int, get_line().split()),
    ]
    second_row = int(get_line())
    second_grid = [
        map(int, get_line().split()),
        map(int, get_line().split()),
        map(int, get_line().split()),
        map(int, get_line().split()),
    ]
    possible_cards = determine_card(first_row - 1, first_grid, second_row - 1, second_grid)
    print "Case #%s:" % case,
    if len(possible_cards) == 1:
        print possible_cards[0]
    elif len(possible_cards) == 0:
        print "Volunteer cheated!"
    else:
        print "Bad magician!"
