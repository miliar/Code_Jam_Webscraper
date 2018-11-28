import math
import fractions

input_file = open('input01.txt', 'r')
output_file = open('output01.txt', 'w')

case_number = int(input_file.readline())

for i, j in enumerate(input_file):
    i += 1
    j = j.split('/')
    k = float(j[0]) / float(j[1])
    l = math.log(float(j[1]) / fractions.gcd(int(j[0]), int(j[1])), 2)

    if l != int(l):
        k = 1
        count = 'impossible'
    else:
        count = 0

    while k < 1:
        k *= 2
        count += 1

    output_file.write('Case #' + str(i) + ': ' + str(count) + '\n')

#output_file.write('Case #' + str(i + 1) + ': ' + str(case_result) + '\n')
