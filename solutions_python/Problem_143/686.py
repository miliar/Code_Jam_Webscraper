__author__ = 'arthurnum'


input = open('B-small-attempt0.in', 'r')
output = open('output.out', 'w')

cases = int(input.readline())

for case in range(cases):
    values = input.readline().split()
    a = int(values[0])
    b = int(values[1])
    k = int(values[2])
    p = 0
    for x1 in range(a):
        for x2 in range(b):
            if x1 & x2 < k:
                p += 1
    output.write("Case #%d: %d\n" % (case + 1, p))

input.close()
output.close()