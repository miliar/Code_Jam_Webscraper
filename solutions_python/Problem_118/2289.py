from math import sqrt
import sys

__author__ = 'Saran'


def main(input_file, output_file):
    file_input = open(input_file)
    file_output = open(output_file, 'w')
    case = int(file_input.readline())
    for count_case in range(0, case):
        #Initial
        count = 0
        #Get N,M
        first_line = file_input.readline().split(' ')
        min = int(first_line[0])
        max = int(first_line[1])
        for num in xrange(min, max + 1):
            if str(num) == str(num)[::-1] and sqrt(num) % 1 == 0:
                if str(int(sqrt(num))) == str(int(sqrt(num)))[::-1]:
                    count += 1
                    print "Check :", num, 'is Palindrome and square [' + str(int(sqrt(num))) + '].'
        print "Case #" + str(count_case + 1) + ':', count
        file_output.writelines("Case #" + str(count_case + 1) + ': ' + str(count))
        if count_case < case - 1:
            file_output.write('\n')



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
