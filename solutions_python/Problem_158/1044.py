def answer(case, ans):
    print("Case #{0}: {1}".format(case, ans))

FAIL = "RICHARD"
WIN = "GABRIEL"
"""
    1: 1
    2: 1
    3: 2
    4: 5
    5: 12
"""

def solve(size, x, y):
    if size == 1:
        return WIN
    if (x * y) % size != 0:
        return FAIL
    elif size == 2:
        if (x * y) % 2 == 0:
            return WIN
    elif size == 3:
        bent = (x == 2 and y == 3) or (x == 3 and y == 2)
        more = (x == 4 and y == 3) or (x == 3 and y == 4)
        wat = (x == 3 and y == 3)
        if bent or more or wat:
            return WIN
    elif size == 4:
        if (x == 3 and y == 4) or (x == 4 and y == 3) or (x == y == 4):
            return WIN
    elif size >= 7:
        return FAIL
    elif size % 2:
        half = size / 2
        if x > half or y > half:
            return FAIL
    else:
        half = (size // 2) + 1
        if x > half or y > half:
            return FAIL
    return FAIL


def main():
    case = 1
    num_cases = int(input())
    while case <= num_cases:
        data = [int(x) for x in input().split()]
        size = data[0]
        grid_x = data[1]
        grid_y = data[2]
        result = solve(size, grid_x, grid_y)
        answer(case, result)
        case += 1

if __name__ == '__main__':
    main()
