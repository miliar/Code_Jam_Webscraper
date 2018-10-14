filename = "B-small-attempt0.in"

f = open(filename)
count = int(f.readline())

def str_list_int(l):
    return map(lambda x: int(x), l.split(' '))

def max_horizontal(x, field):
    val = 0
    for i in range(len(field[0])):
        cell = field[x][i]
        if val < cell:
            val = cell
    return val

def max_vertical(y, field):
    val = 0
    for i in range(len(field)):
        cell = field[i][y]
        if val < cell:
            val = cell
    return val

def check(field):
    len_x = len(field)
    len_y = len(field[0])
    for i in range(len_x):
        for j in range(len_y):
            cell = field[i][j]
            if max_horizontal(i, field) > cell and \
                max_vertical(j, field) > cell:
                return False
    return True

for i in range(count):
    x, y = str_list_int(f.readline())
    field = []
    for j in range(x):
        field.append(str_list_int(f.readline()))

    if check(field):
        print "Case #%s: YES" % (i+1)
    else:
        print "Case #%s: NO" % (i+1)
