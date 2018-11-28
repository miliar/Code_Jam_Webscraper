import math

def is_palindrone(i):
    if type(i) == int:
        i = str(i)    
    back = i[::-1]
    return int(i) == int(back)

def get_square_int(i):
    if type(i) != int:
        i = int(i)
    f = math.sqrt(i)
    i = int(f)
    return i

def is_square(i):
    if type(i) != int:
        i = int(i)
    f = math.sqrt(i)
    i = int(f)
    return f == float(i)


f = open("C-small-attempt1.in", "r")
lines = f.readlines()

n = int(lines[0].strip())
i = 1
for line in lines[1:]:
    v = 0
    limits = line.strip().split(" ")
    _min = int(limits[0])
    _max = int(limits[1])+1
    for j in range(_min, _max):
        if is_palindrone(j) and is_square(j) and is_palindrone(get_square_int(j)):
            v += 1
    print "Case #%d: %d" % (i, v)
    i += 1
