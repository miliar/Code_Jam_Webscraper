def scan_number(number):
    min_digit = max_digit = -1
    digits = set()
    for index in range(len(number))[::-1]:
        digit = number[index]
        digits.add(digit)
        if min_digit == -1:
            min_digit = digit
            max_digit = digit
        elif digit < min_digit:
            higher_digit_index = number.rfind(min_digit)
            between_digits = number[index:higher_digit_index]
            post_digits = number[higher_digit_index+1:]
            return number[:index] + min_digit + ''.join(sorted(between_digits + post_digits))
        else:
            if digit < max_digit:
                higher_digit = max_digit
                for other_digit in digits:
                    if other_digit > digit and other_digit < higher_digit:
                        higher_digit = other_digit
                higher_digit_index = number.rfind(higher_digit)
                between_digits = number[index:higher_digit_index]
                post_digits = number[higher_digit_index+1:]
                return number[:index] + higher_digit + ''.join(sorted(between_digits + post_digits))
            else:
                max_digit = digit
    number = ''.join(sorted(number))
    zeros = []
    while number[0] == '0':
        zeros.append('0')
        number = number[1:]
    number = number[0] + ''.join(zeros) + number[1:]
    return number[0] + '0' + number[1:]
            

def process(in_file):
    in_file = open(in_file)
    T = int(in_file.readline().strip())
    for test_num in range(T):
        number = in_file.readline().strip()
        print 'Case #%d: %s' % (test_num + 1, scan_number(number))

if __name__ == '__main__':
    import sys
    #import numpy
    #a = numpy.repeat([0,1,2,3,4,5,6,7,8,9], 10)
    #for i in range(10):
    #    number = ''.join(map(repr, numpy.random.permutation(a)))[:10]
    #    print '%s - %s' % (number, scan_number(number))
    process(sys.argv[1])
    #print scan_number('511')
