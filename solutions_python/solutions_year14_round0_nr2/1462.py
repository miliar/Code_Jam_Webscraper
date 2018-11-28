__author__ = 'antonkov'

input = open('input', 'r')

def read_int():
    return int(input.readline())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_floats():
    return [float(x) for x in input.readline().split()]

t = read_int()
for test in range(t):
    print("Case #" + str(test + 1) + ": ", end="")
    c, f, x = read_floats()
    speed = 2
    time = 0
    while True:
        cur = x / speed
        can = x / (speed + f) + c / speed
        if can < cur:
            time += c / speed
            speed += f
        else:
            time += x / speed
            break
    print("%.10f" % time)