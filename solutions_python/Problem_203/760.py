tests = int(input())


def problem():
    dims = input().split()
    r, c = int(dims[0]), int(dims[1])
    lines = [input() for _ in range(0, r)]
    chars = list(set(''.join(lines)))
    return solve(lines, chars)[1]


def solve(lines, chars):
    if chars == [] or chars == ['?']:
        return '?' not in ''.join(lines), lines
    char = chars[0]
    if char == '?':
        char = chars[1]
    chars_new = [c for c in chars if c != char]
    #print(char)
    for cut in get_possible_cuts(lines, char):
        s, l = solve(cut, chars_new)
        if s:
            return s, l
    return False, lines


def get_possible_cuts(lines, char):
    x, y = [(ix, iy) for ix, row in enumerate(lines) for iy, i in enumerate(row) if i == char][0]
    return get_available_cuts(lines, char, x, y, 1, 1)


def get_available_cuts(lines, char, x, y, w, h):
    #print("x " + str(x) + " y " + str(y) + " w " + str(w) + " h " + str(h))
    cuts = [lines]
    # up
    if y > 0:
        l = lines[:]
        valid = True
        for w1 in range(0, w):
            if l[x + w1][y-1] != '?':
                valid = False
                break
            l[x+w1] = l[x+w1][0:y-1] + char + l[x+w1][y:]
        if valid:
            #print("up")
            cuts += get_available_cuts(l, char, x, y-1, w, h+1)
    # down
    if (y+h) < len(lines[0]):
        l = lines[:]
        valid = True
        for w1 in range(0, w):
            if l[x+w1][y+h] != '?':
                valid = False
                break
            l[x+w1] = l[x+w1][0:y+h] + char + l[x+w1][y+h+1:]
        if valid:
            #print("down")
            cuts += get_available_cuts(l, char, x, y, w, h+1)
    # left
    if x > 0:
        l = lines[:]
        valid = True
        for h1 in range(0, h):
            if l[x-1][y+h1] != '?':
                valid = False
                break
            l[x-1] = l[x-1][0:y+h1] + char + l[x-1][y+h1+1:]
        if valid:
            #print("left")
            cuts += get_available_cuts(l, char, x-1, y, w+1, h)
    # right
    if (x+w) < len(lines):
        l = lines[:]
        valid = True
        for h1 in range(0, h):
            if l[x+w][y+h1] != '?':
                valid = False
                break
            l[x+w] = l[x+w][0:y+h1] + char + l[x+w][y+h1+1:]
        if valid:
            #print("right")
            cuts += get_available_cuts(l, char, x, y, w+1, h)
    return cuts

for t in range(1, tests + 1):
    prob = problem()
    print("Case #{}:".format(t))
    for probline in prob:
        print(probline)
