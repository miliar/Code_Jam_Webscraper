MAX_ALT = 10000

def read_file(filename):
    f = open(filename)
    contents = f.read().splitlines()
    return contents

contents = read_file('B-large.in')
T = int(contents.pop(0))

def process_map(case, w, h, map):
    print 'Case #%d:' % case
    letter_map = []
    for y in xrange(h):
        letter_map.append([])
        for x in xrange(w):
            letter_map[-1].append('')

    def get_neighbors(x, y):
        neighbors = (
            (x, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x, y + 1),
        )
        for nx, ny in neighbors:
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            yield (nx, ny)

    def get_best(x, y):
        min = MAX_ALT + 1
        mx, my = -1, -1
        for nx, ny in get_neighbors(x, y):
            if map[ny][nx] < map[y][x] and map[ny][nx] < min:
                min = map[ny][nx]
                mx, my = nx, ny
        if min <= MAX_ALT:
            return (mx, my)
        else:
            return None

    def proceed_from(x, y, letter):
        if letter_map[y][x]:
            return False
        letter_map[y][x] = letter
        best = get_best(x, y)
        if best:
            proceed_from(best[0], best[1], letter)
        for nx, ny in get_neighbors(x, y):
            if get_best(nx, ny) == (x, y):
                proceed_from(nx, ny, letter)
        return True

    letter = 'a'
    for y in xrange(h):
        for x in xrange(w):
            if proceed_from(x, y, letter):
                letter = chr(ord(letter) + 1)
                    
    for row in letter_map:
        print ' '.join(row)

for i in xrange(T):
    H, W = [int(x) for x in contents.pop(0).split()]
    map = [[int(y) for y in x.split()] for x in contents[:H]]
    process_map(i + 1, W, H, map)
    contents = contents[H:]
