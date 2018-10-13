import numpy as np

# Problem 2: Tidy Numbers
# CodeJam 2017 Qualification
# By: Richard Salas Chavez

def main():
    input = open('B-large.in','r')
    output = open('B-output-large.txt', 'w')

    test_cases = int(input.readline()) # number of test cases
    print test_cases
    print
    case = 1
    # loop through cases
    while(case <= test_cases):
        print case
        first = -1
        num = int(input.readline().strip())
        str_num = str(num)
        digits_list = [int(n) for n in str_num]
        print num
        num_digits = len(digits_list)

        if num_digits == 1:
            output.write("Case #%i: %i\n" % (case, num))
            print num
            print
        else:
            first = -1
            equal = 0
            for i in range(len(digits_list)-1):
                d1 = digits_list[i]
                d2 = digits_list[i+1]

                if d1 == d2:
                    equal += 1
                if d1 > d2:
                    first = i
                    break
                elif d1 != d2:
                    equal = 0

            if first == -1:
                output.write("Case #%i: %i\n" % (case, num)) # all equal
                print num
                print
            else:
                if equal > 0: # there are a bunch of equal number
                    equal += 1
                    special = False
                    if digits_list[first+1] == 0 and digits_list[first] == 1:
                        special = True
                    first = first - (equal-1)
                    digits_list[first] -= 1

                    if special:
                        for i in range(1,equal-1):
                            index = first - i
                            digits_list[index] = 9
                else:
                    digits_list[first] -= 1

                if digits_list[first] + 1 == 0:
                    digits_list[first] = 0
                    for i in range(first + 1, len(digits_list)):
                        digits_list[i] = 0
                else:
                    for i in range(first+1,len(digits_list)):
                        digits_list[i] = 9

                s = filter(str.isdigit, repr(digits_list))
                num = int(s)
                print num
                output.write("Case #%i: %i\n" % (case, num))
                print

        case += 1

    input.close()
    output.close()

main()