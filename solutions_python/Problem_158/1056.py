cases = int(raw_input())
case = 1


def get_biggest_possible_height_and_width(x):
    # TODO: For large input we will need to really calculate this
    if x == 1:
        return 1, 1
    elif x == 2:
        return 2, 1
    elif x == 3:
        return 2, 2
    elif x == 4:
        return 2, 3


while cases > 0:
    reqs = raw_input().split(" ")
    x = int(reqs[0])
    r = int(reqs[1])
    c = int(reqs[2])

    winner = ""

    # X - omino size
    # R - rows in grid
    # C - cols in grid

    # The grid
    # [
    #     ['.', '.', '.', '.'],
    #     ['.', '.', '.', '.'],
    #     ['.', '.', '.', '.'],
    #     ['.', '.', '.', '.'],
    # ]

    # empty_grid = [[] for i in range(0, r)]
    # for row in empty_grid:
    #     for i in range(0, c):
    #         row.append('.')
    # print empty_grid

    # Quick check to make sure it isn't impossible
    # for gabriel to win no matter what
    total_squares = r*c
    if total_squares % x != 0:
        winner = "RICHARD"
    # Richard at least has a chance
    else:
        max_omino_area = get_biggest_possible_height_and_width(x)
        max_height = max_omino_area[0]
        max_width = max_omino_area[1]

        min_of_the_max_area = min(max_height, max_width)
        min_width_or_height_of_grid = min(r, c)

        max_of_the_max_area = max(max_height, max_width)
        max_width_or_height_of_grid = max(r, c)

        area = r*c
        max_area_of_omino = max_width*max_height
        # If it is possible to make an omino that is bigger than the 
        # width or height of the grid there is no way for the chosen
        # piece to even fit the grid so richard wins
        if min_of_the_max_area > min_width_or_height_of_grid:
            winner = "RICHARD"
        elif max_of_the_max_area > max_width_or_height_of_grid:
            winner = "RICHARD"
        # Check for forced holes
        elif min_of_the_max_area == min_width_or_height_of_grid and x > 3:
            winner = "RICHARD"
        # Otherwise richard can't choose an impossible piece from the start
        # so we need to simulate this thing or assume gabriel wins
        else:
            # TODO: For large input we need to simulate this thing or do
            # something else a little smarter
            winner = "GABRIEL"




    print("Case #{0}: {1}".format(str(case), winner))
    case+=1
    cases-=1

