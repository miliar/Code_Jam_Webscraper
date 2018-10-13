fname = 'C-small-attempt0.in'
with open(fname) as f:
    content = f.readlines()

total = int(content.pop(0))

case = 0

import math
def fair_and_square(number):
    if not number[::-1] == number: #palyndrome
        return False
    square = math.sqrt(int(number))
    if not square.is_integer(): #square
        return False
    square = str(int(square))
    
    return square[::-1] == square #fair

while(case < total):
    numbers = content[case].strip().split(' ')
    numbers = range(int(numbers[0]), int(numbers[1])+1)
    f_n_squares = 0
    for number in numbers:
        if fair_and_square(str(number)):
            f_n_squares += 1
    print 'Case #%d: %d' % (case+1, f_n_squares)
    case += 1
