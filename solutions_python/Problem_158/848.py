from copy import deepcopy
import pprint


def check_tile_fit(fields_checked_for_modulo, tile, map, i, j, X):
    for k in range(X):
        for l in range(X):
            try:
                if (i + k > X) or (j + l > X) or (tile[k][l] and map[i + k][j + l]):
                    return False
            except IndexError:
                return False
    for k in range(X):
        for l in range(X):
            if tile[k][l]:
                fields_checked_for_modulo[i + k][j + l] = True
    return True


def pivoted_area_expand(i, j, fields_checked_for_modulo, pivot_area, R, C, X):
    fields_checked_for_modulo[i][j] = True
    pivot_area[i][j] = True
    if not fields_checked_for_modulo[i - 1][j]:
        pivoted_area_expand(i - 1, j, fields_checked_for_modulo, pivot_area, R, C, X)
    if not fields_checked_for_modulo[i + 1][j]:
        pivoted_area_expand(i + 1, j, fields_checked_for_modulo, pivot_area, R, C, X)
    if not fields_checked_for_modulo[i][j - 1]:
        pivoted_area_expand(i, j - 1, fields_checked_for_modulo, pivot_area, R, C, X)
    if not fields_checked_for_modulo[i][j + 1]:
        pivoted_area_expand(i, j + 1, fields_checked_for_modulo, pivot_area, R, C, X)


def try_to_land(tile, map, R, C, X):
    for j in range(R):
        for i in range(C):
            fields_checked_for_modulo = deepcopy(map)
            if check_tile_fit(fields_checked_for_modulo, tile, map, i + 1, j + 1, X):
                for l in range(R):
                    breaked = False
                    for k in range(C):
                        if fields_checked_for_modulo[k + 1][l + 1]:
                            continue
                        pivot_area = [[False for x in range(R + 2)] for y in range(C + 2)]
                        pivoted_area_expand(k + 1, l + 1, fields_checked_for_modulo, pivot_area, R, C, X)
                        area = 0
                        for n in range(R):
                            for m in range(C):
                                if pivot_area[m + 1][n + 1]:
                                    area += 1
                        if area % X == 0:
                            continue
                        breaked = True
                        break
                    if breaked:
                        break
                else:
                    return True


def generate_map(R, C):
    one_bigger = [[False for x in range(R + 2)] for y in range(C + 2)]
    for x in range(R + 2):
        one_bigger[0][x] = True
        one_bigger[C+1][x] = True
    for x in range(C + 2):
        one_bigger[x][0] = True
        one_bigger[x][R+1] = True
    return one_bigger


def generate_tiles(X):
    actual_tile = [[False for x in range(X)] for x in range(X)]
    for j in range(X):
        actual_tile[0][j] = True
    yield actual_tile
    actual_tile[0][X - 1] = False
    before_row_max_column = X - 1
    for actual_row in range(1, X):
        j = 0
        while before_row_max_column >= j:
            actual_tile[actual_row - 1][before_row_max_column] = False
            for actual_column in range(before_row_max_column, j, -1):
                actual_tile[actual_row][actual_column] = False
                actual_tile[actual_row][actual_column - 1] = True
                yield actual_tile
            before_row_max_column -= 1
            j += 1


T = int(input())
for case in range(T):
    (X, R, C) = map(int, raw_input().split(' '))
    if not ((R * C) % X == 0):
        print("Case #%d: RICHARD" % (case + 1))
        continue
    if X <= 2:
        print("Case #%d: GABRIEL" % (case + 1))
        continue
    half_counter = (R * C) / 2
    higher = max(R, C)
    permutations = [(i, j) for i in range(higher) for j in range(higher)]
    outer_continue = False
    for (i, j) in permutations:
        if not (i + j) == X:
            continue
        if (i > R and j > R) or (i > C and j > C):
            print("Case #%d: RICHARD" % (case + 1))
            outer_continue = True
            break
        half_counter -= 1
        if half_counter == 0:
            break
    if outer_continue:
        continue
    for tiles in generate_tiles(X):
        if not try_to_land(tiles, generate_map(R, C), R, C, X) and not try_to_land(tiles, generate_map(C, R), C, R, X):
            print("Case #%d: RICHARD" % (case + 1))
            break
    else:
        print("Case #%d: GABRIEL" % (case + 1))
