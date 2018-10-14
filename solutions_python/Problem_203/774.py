from copy import deepcopy

cake = []
r = 0
c = 0

def is_expandable(x1, y1, x2, y2):
    if x1 < 0 or y1 < 0 or x2 >= r or y2 >= c:
        return False
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if cake[i][j] is not '?':
                return False
    return True

def expand_to(x1, y1, x2, y2, x, y):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            cake[i][j] = cake[x][y]

def expand(cake, x, y):
    bottom_expandable = True
    right_expandable = True
    top_expandable = True
    left_expandable = True
    bottom = x
    top = x
    right = y
    left = y
    for t in range(1, 25):
        if bottom_expandable:
            if is_expandable(bottom + 1, left, bottom + 1, right):
                expand_to(bottom + 1, left, bottom + 1, right, x, y)
                bottom += 1
            else:
                bottom_expandable = False
        if right_expandable:
            if is_expandable(top, right + 1, bottom, right + 1):
                expand_to(top, right + 1, bottom, right + 1, x, y)
                right += 1
            else:
                right_expandable = False
        if top_expandable:
            if is_expandable(top - 1, left, top - 1, right):
                expand_to(top - 1, left, top - 1, right, x, y)
                top -= 1
            else:
                top_expandable = False
        if left_expandable:
            if is_expandable(top, left - 1, bottom, left - 1):
                expand_to(top, left - 1, bottom, left - 1, x, y)
                left -= 1
            else:
                left_expandable = False
        if not (bottom_expandable or right_expandable or top_expandable or left_expandable):
            break

if __name__ == '__main__':
    with open('A-small-attempt1.in', 'r') as file:
        test_cases = int(file.readline())
        for case_no in range(test_cases):
            size = file.readline().split()
            r = int(size[0])
            c = int(size[1])
            cake = []
            for x in range(r):
                cake.append([])
                row = file.readline()
                for y in range(c):
                    cake[x].append(row[y])
            original_cake = deepcopy(cake)
            print('Case #' + str(case_no + 1) + ':')
            for x in range(r):
                for y in range(c):
                    if original_cake[x][y] is not '?':
                        expand(cake, x, y)
            for x in range(r):
                line = ''
                for y in range(c):
                    line += cake[x][y]
                print(line)

