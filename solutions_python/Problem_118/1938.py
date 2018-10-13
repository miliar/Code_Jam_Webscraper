input_file = open('C:\Programs\programing\python26\contest2013\C-small-attempt0.in', 'r')
output_file = open('C:\Programs\programing\python26\contest2013\C-small-attempt0.out', 'w')
from math import sqrt, ceil, floor

number_inputs = 0
current_input = 1
s_poly_array =[]
poly_array = []

def poly_up_to(length):
    arr = []
    if length == 1:
        for i in range(0,10):
            arr.append(str(i))
    else:
        for j in poly_up_to(length-1):
            arr.append(j)
    
    if length == 2:
        for i in range(0,10):
            arr.append(str(i)*2)
    elif length > 2:
        for i in range(1,10):
            s_i = str(i)
            for j in poly_up_to(length-2):
                arr.append(s_i + j + s_i)
    return arr


def is_poly(x):
    n = str(x)
    ln = len(n)
    for i in range(ln //2):
        if n[i] != n[ln-i-1]:
            return False
    return True

s_poly_array = poly_up_to(len(str(10**5)))
s_poly_array.remove('0')
s_poly_array.remove('00')
for i in s_poly_array:
    poly_array.append(int(i))

for line in input_file:
    if number_inputs==0:
        number_inputs = int(line)
    elif line == '\n':
        pass
    else:
        count = 0
        bounds = line.split()
        low, high = int(bounds[0]), int(bounds[1])
        sqr_low = ceil(sqrt(low))
        sqr_high = floor(sqrt(high))
        for poly in poly_array:
            if poly <= sqr_high and poly >= sqr_low and is_poly(poly**2):
                count+= 1
        output_file.write('Case #' + str(current_input) + ': ' + str(count))
        if current_input != number_inputs:
            current_input += 1
            output_file.write('\n')



input_file.close()
output_file.close()
