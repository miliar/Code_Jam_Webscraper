import math

lines = open('C-small-attempt0.in').read().splitlines()

num_cases = int(lines[0])

wining_seq = []

output = []

def perfect_squares(min, max):
    lowest = int(math.ceil(math.sqrt(min)))
    heighest = int(math.sqrt(max))
    return (n**2 for n in range(lowest, heighest + 1))


for i in range(num_cases):
    start = i + 1
    m, n = lines[start].split(' ')
    a, b = int(m), int(n)

    squares = perfect_squares(a,b)

    res = []
    for sq in squares:
        s = str(sq)
        if s == s[::-1]:
            sqrt = str(int(math.sqrt(sq)))
            if sqrt == sqrt[::-1]:
                res.append(sq)

    print res
    output.append(len(res))

o_file = open('C-small-attempt0.out', 'w+')
for i in range(num_cases):
    o_file.write("Case #%s: %s\n" % ( str(i+1), output[i] ))