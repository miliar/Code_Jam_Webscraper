import sys
import math
import pprint


def process_input(input):
    return [(int(i[0]),int(i[1])) for i in [
        e.strip().split() for e in list(input)[1:]] if i
    ]



def is_palindome(number):
    number_string = str(number).split(".")[0][::-1]
    return number_string == number_string[::-1]

def is_square_palindome(number):
    square_number = math.sqrt(number)
    if square_number.is_integer():
        return is_palindome(square_number)
    return False

for i, case in enumerate(process_input(sys.stdin),1):
    A, B = case
    result = len([e for e in range(A, B+1) if is_square_palindome(e) and is_palindome(e)])
    print "Case #%s: %s" % (i,result)

