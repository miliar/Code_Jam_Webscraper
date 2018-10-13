__author__ = 'vaibhav'

f = open('B-small-attempt0.in')
f1 = open('output2B.txt', 'w')

no_of_cases = int(f.readline())

for i in range(0, no_of_cases):
    values = f.readline()
    values = list(map(int, values.strip().split(' ')))
    v1 = values[0]
    v2 = values[1]
    count = 0
    for i1 in range(0, v1):
        for j in range(0, v2):
            if i1 & j < values[2]:
                count += 1

    string = 'Case #%d: %d' % (i+1, count)
    f1.write(string + '\n')
f.close()
f1.close()

