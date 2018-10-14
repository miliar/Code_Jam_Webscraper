from math import pi, pow

def circles(r, t):
    constant = 2*r
    index = 1
    total = 0 
    while t > 0:
        t -= (constant+pow(index, 2)-pow(index-1, 2)) 
        index += 2
        if t>=0:
            total += 1
    return total

def read_input(filename):
    f = open(filename)
    tests_number = int(f.readline())
    for i in xrange(tests_number):
        vals = map(int, f.readline()[:-1].split())
        yield(i+1, vals[0], vals[1])

input = read_input('A-small-attempt0.in')
output_file = open('bulls_eye.out', "w")

for test in input:
    result = "Case #%d: %d\n" % (test[0], circles(test[1], test[2]))
    output_file.write(result)
