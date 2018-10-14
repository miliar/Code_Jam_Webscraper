import math

in_data = open('A-large.in').readlines()
in_data = [x.strip() for x in in_data]
T = int(in_data[0])
in_data = in_data[1:]


res = open('result', 'w')
case_no = 0
for line in in_data:
    case_no += 1
    r, t = [int(x) for x in line.split()]
    r = 2*r + 1
    n = int((2-r + math.sqrt((2-r)*(2-r) + 8 *t))/4)
    while (2 * n * n + (r-2)*n < t):
            n = n + 1    
    while (2 * n * n + (r-2)*n > t):
        n = n-1
    
    output = 'Case #' + str(case_no) + ': ' + str(n) + '\n'
    res.write(output)