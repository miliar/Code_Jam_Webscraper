# def is_tidy(n):
#     n = str(n)
#     previous = ''
#     for c in n:
#         if c < previous:
#             return False
#         previous = c
#     return True

file = 'B-large.in'
file2 = file + '.out'
g = open(file2,'w')

with open(file, 'r') as f:
    f.readline()
    i = 1
    for line in f:
        j = 0
        number = []
        line = line.strip()
        line = line[::-1]
        previous = line[0]
        for c in line:
            if c > previous:
                new = str(int(c)-1)
                number.append(new)
                number[0:j] = ['9'] * j
                previous = new
            else:
                number.append(c)
                previous = c
            j += 1

        number = number[::-1]
        number = ''.join(number)
        print('Case #{0}: {1}'.format(i, number.lstrip('0')),file=g)
        i += 1


