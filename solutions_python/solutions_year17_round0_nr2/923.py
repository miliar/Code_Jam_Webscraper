import sys

'''
This funcion is adapted from here
http://stackoverflow.com/questions/974952/split-an-integer-into-digits-to-compute-an-isbn-checksum
'''
def get_list_of_digits(number):
    result = list()
    while number:
        digit = number % 10
        result.insert(0, digit)
        number //= 10
    return result

#print get_list_of_digits(3345)

def get_number(digits):
    result = 0
    for index, digit in enumerate(digits):
        result += digit*(10**(len(digits)-index-1))
    return result

#print get_number([1,2,3,4])

def check_if_tidy(digits):
    index = 0
    while index+1 < len(digits) and digits[index]<= digits[index+1]:
        index += 1
    return index


def tidy_up(digits):
    index = check_if_tidy(digits)
    if index is len(digits)-1:
        return digits
    elif digits[index] > 1:
        jindex = index-1
        while jindex >= 0 and digits[jindex] == digits[index]:
            jindex -= 1
        index = jindex + 1
        digits[index] -= 1
        for jindex in range(index+1, len(digits)):
            digits[jindex]=9
    else: digits = [9]*(len(digits)-1)
    return digits

#print tidy_up(get_list_of_digits(983))



if __name__ == "__main__" and len(sys.argv) is 2:
    filename = sys.argv[1]
    infile = open(filename+".in", "r")
    outfile = open(filename+".out", "w")
    T = int(infile.readline())
    for case in range(T):
        number = int(infile.readline())
        digits = get_list_of_digits(number)
        tidy_digits = tidy_up(digits)
        tidy_number = get_number(tidy_digits)
        outfile.write("Case #{}: {}\n".format(case+1, tidy_number))
    infile.close()
    outfile.close()
