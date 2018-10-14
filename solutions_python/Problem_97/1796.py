import sys

def count_digits(number):
    digits = 0
    while number > 0:
        number /= 10
        digits += 1
    return digits

def num_as_list(number):
    strn = str(number)
    num_list = []
    for char in strn:
        num_list.append(char)
    return num_list

def list_as_num(num_list):
    return int(''.join(num_list))

def permute(case, a, b):
    results = []
    digits = count_digits(a)
    for x in xrange(a, b):
        num_list = num_as_list(x)

        for offset in range(digits):
            comparator = [None] * digits
            # shift round
            for index in range(len(num_list)):
                comparator[(index+offset)%len(num_list)] = num_list[index]
            comp_num = list_as_num(comparator)
            if comp_num > x and comp_num <= b:
                results.append((x,comp_num,))
                # print '%s and %s' % (x, comp_num)
    print 'Case #%s: %s' % (case,len(set(results)))

std_in = sys.stdin.readlines()
cases = int(std_in.pop(0))

for index, line in enumerate(std_in):
    tokens = line.split()
    a = int(tokens[0])
    b = int(tokens[1])
    permute(index+1, a, b)
