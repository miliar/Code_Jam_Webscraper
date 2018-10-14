# Code Jam 2010
# Round 2
# Problem C

IN = 'E:\cj\in\C-small.in'
OUT = 'E:\cj\out\c.out'

fin = open(IN, 'r')
fout = open(OUT, 'w')

cases = int(fin.readline())

MAX = 100 + 1

def blank_field(max_x = MAX, max_y = MAX):
    return [[0 for i in xrange(max_x + 2)] for j in xrange(max_y + 2)]

def print_field(field, max_x, max_y):
    for row in field[1:max_y + 2]:
        print ''.join(map(str, row[1:max_x + 2]))

# gonna simulate it
for case in xrange(1, cases + 1):
    print case
    max_x = 0
    max_y = 0
    R = int(fin.readline())
    field = blank_field()  
    for r in xrange(R):
        x1, y1, x2, y2 = map(int, fin.readline().split())

        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
        
        for x in xrange(x1, x2 + 1):
            for y in xrange(y1, y2 + 1):
                field[y][x] = 1

    field_dead = False
    T = 0

    while not field_dead:
#        print_field(field, max_x, max_y)
#        print '*'
        field_dead = True if sum(map(sum, field)) == 0 else False
        if not field_dead:
            T += 1
            new_field = blank_field(max_x, max_y)
            for x in xrange(1, max_x + 1):
                for y in xrange(1, max_y + 1):
                    if field[y][x]:
                        new_field[y][x] = 1 if field[y - 1][x] or field[y][x - 1] else 0
                    else:
                        new_field[y][x] = 1 if field[y - 1][x] and field[y][x - 1] else 0
            field = new_field

    fout.write('Case #%d: %d\n' % (case, T))

fin.close()
fout.close()
