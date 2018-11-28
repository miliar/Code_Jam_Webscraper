def test_up():
    for i in range(r - 1, -1, -1):
        if grid[i][c] != '.':
            return True
    else:
        return False

def test_right():
    for i in range(c + 1, C):
        if grid[r][i] != '.':
            return True
    else:
        return False

def test_down():
    for i in range(r + 1, R):
        if grid[i][c] != '.':
            return True
    else:
        return False

def test_left():
    for i in range(c - 1, -1, -1):
        if grid[r][i] != '.':
            return True
    else:
        return False

for t in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    ans = 0
    grid = [input() for _ in range(R)]
    for r in range(R):
        for c in range(C):
            cell = grid[r][c]
            now = r * C + c
            if cell == '^':
                if not test_up():
                    if test_down() or test_left() or test_right():
                        ans += 1
                    else:
                        ans = -1
                        break
            elif cell == '>':
                if not test_right():
                    if test_up() or test_down() or test_left():
                        ans += 1
                    else:
                        ans = -1
                        break
            elif cell == 'v':
                if not test_down():
                    if test_up() or test_left() or test_right():
                        ans += 1
                    else:
                        ans = -1
                        break
            elif cell == '<':
                if not test_left():
                    if test_down() or test_up() or test_right():
                        ans += 1
                    else:
                        ans = -1
                        break
        if ans == -1:
            print('Case #%d: IMPOSSIBLE' % t)
            break
    else:
        print('Case #%d: %d' % (t, ans))
