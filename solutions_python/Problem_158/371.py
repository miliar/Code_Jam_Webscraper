def solve(x, r, c):
    area = r * c

    if x == 1:
        return "GABRIEL"
    if x == 2:
        if area % 2 == 0:
            return "GABRIEL"
        return "RICHARD"
    if x == 3:
        if area % x == 0 and area != 3:
            return "GABRIEL"
        return "RICHARD"
    if x == 4:
        if area == 12 or area == 16:
            return "GABRIEL"
        return "RICHARD"

if __name__ == '__main__':
    f = open('input')
    n = int(f.readline().rstrip())

    for case in range(n):
        x, r, c = map(int, f.readline().rstrip().split())
        print('Case #{0}: {1}'.format(case + 1, solve(x, r, c)))
