'''
Created on Apr 13, 2013

@author: Federico
'''
from math import sqrt
def palindrome(number):
    a = str(number)
    return a == a[::-1]

lst_number = [line.strip() for line in open('C-small-attempt0.in', "r")]
file_solution = open('result.txt', 'w')

number_test = int(lst_number.pop(0))

for i in range(1, number_test + 1):
    x, y = map(int, lst_number.pop(0).split())
    x_root = int(sqrt(x))
    y_root = int(sqrt(y))

    fair = 0

    for number in range(x_root, y_root + 1):
        if (palindrome(number) and palindrome(number * number) and
           (number * number) <= y and (number * number) >= x):
            fair += 1
    
    print "Case #%d: %d"%(i, fair)
    file_solution.write("Case #%d: %d\n"%(i, fair))