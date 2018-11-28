#!/usr/bin/env python
# -*- coding: utf-8 -*-

def open_file(file_name):
    with open(file_name) as f:
        case_cnt = int(f.readline())
        case_list = []
        for i in range(0, case_cnt):
            rc = f.readline()
            rc_items = rc.split(" ")
            r = int(rc_items[0])
            c = int(rc_items[1])
            grid = []
            for j in range(0, r):
                c_line = f.readline().strip()
                for c_index, letter in enumerate(c_line):
                    if letter is not "?":
                        grid.append((letter, j, c_index))
            case_list.append((r, c, grid))
        return case_list

def pos_to_index(r, c, rr, cc):
    return (r) * cc + (c)

def solve_one_case(case):
    rr = case[0]
    cc = case[1]
    grid = case[2]

    grid_m = [''] * (rr * cc)

    # find cross letter
    letter_dict = dict()
    for letter, r, c in grid:
        if letter in letter_dict:
            pos = letter_dict[letter]
            minr, minr, maxc, maxc = pos
            if r < minr:
                minr = r
            if r > maxr:
                maxr = r
            if c < minc:
                minc = c
            if c > maxc:
                maxc = c
            letter_dict[letter] = (minr, minr, maxc, maxc)
        else:
            letter_dict[letter] = (r, c, r, c)

    # fill all cross letter
    for letter, grid in letter_dict.items():
        minr, minc, maxr, maxc = grid
        for r in range(minr, maxr + 1):
            for c in range(minc, minc + 1):
                index = pos_to_index(r, c, rr, cc)
                grid_m[index] = letter

    # expand all
    for letter in letter_dict:
        pos = letter_dict[letter]
        minr, minc, maxr, maxc = pos

        # minr
        # up
        while(True):
            minr -= 1
            if minr < 0:
                minr += 1
                break
            else:
                valid = True
                for i in range(minc, maxc + 1):
                    index = pos_to_index(minr, i, rr, cc)
                    if grid_m[index] != '':
                        valid = False
                        break
                if valid == True:
                    for i in range(minc, maxc + 1):
                        index = pos_to_index(minr, i, rr, cc)
                        grid_m[index] = letter
                else:
                    minr += 1
                    break

        # maxr down
        while (True):
            maxr += 1
            if maxr >= rr:
                maxr -= 1
                break
            else:
                valid = True
                for i in range(minc, maxc + 1):
                    index = pos_to_index(maxr, i, rr, cc)
                    if grid_m[index] != '':
                        valid = False
                        break
                if valid == True:
                    for i in range(minc, maxc + 1):
                        index = pos_to_index(maxr, i, rr, cc)
                        grid_m[index] = letter
                else:
                    maxr -= 1
                    break

        # minc
        # left
        while (True):
            minc -= 1
            if minc < 0:
                minc += 1
                break
            else:
                valid = True
                for i in range(minr, maxr + 1):
                    index = pos_to_index(i, minc, rr, cc)
                    if grid_m[index] != '':
                        valid = False
                        break
                if valid == True:
                    for i in range(minr, maxr + 1):
                        index = pos_to_index(i, minc, rr, cc)
                        grid_m[index] = letter
                else:
                    minc += 1
                    break

        # maxc
        # right
        while (True):
            maxc += 1
            if maxc >= cc:
                maxc -= 1
                break
            else:
                valid = True
                for i in range(minr, maxr + 1):
                    index = pos_to_index(i, maxc, rr, cc)
                    if grid_m[index] != '':
                        valid = False
                        break
                if valid == True:
                    for i in range(minr, maxr + 1):
                        index = pos_to_index(i, maxc, rr, cc)
                        grid_m[index] = letter
                else:
                    maxc -= 1
                    break

    return (rr, cc, grid_m)

def solve_all(case_list, out_file):
    with open(out_file, 'w') as f:
        for i, case in enumerate(case_list):
            res = solve_one_case(case)
            """
            Case #1:
            GGJ
            CCJ
            CCJ
            Case #2:
            CODE
            COAE
            JJAM
            Case #3:
            CA
            KE
            """
            rr, cc, grid = res
            grid_str_list = []
            for r in range (0, rr):
                r_str = ''
                for c in range(0, cc):
                    r_str += grid[pos_to_index(r, c, rr, cc)]
                grid_str_list.append(r_str)

            line = "Case #" + str(i + 1) + ":\n" + "\n".join(grid_str_list)
            f.write(line)
            f.write("\n")

def solve_test_case():
    case_list = open_file("test_case")
    solve_all(case_list, "test_case_out")

def solve_small_case():
    case_list = open_file("A-small-attempt2.in")
    solve_all(case_list, "A-small-attempt2.out")

def solve_large_case():
    case_list = open_file("A-large.in")
    solve_all(case_list, "A-large.out")

if __name__ == "__main__":
    solve_test_case()
    solve_small_case()
    solve_large_case()

