import fileinput


def is_tidy(number):
    string_representation = str(number)
    last_digit = None
    
    for i, digit in enumerate(string_representation):
        if last_digit is not None and int(digit) < last_digit:
            return False, i
            
        last_digit = int(digit)
       
    return True, -1


def long_xrange(start, stop, step=1):
    while start < stop:
        yield start
        start += step


def last_tidy_number(n):
    while n >= 1:
        result, bad_index = is_tidy(n)
        if result:
            return n
        len(str(n)) - bad_index + 1
        n -= 1


def main():
    input = [line.strip() for line in fileinput.input()]
    case_count = int(input[0])
    
    for i in xrange(1, case_count + 1):
        n = int(input[i])
        result = last_tidy_number(n)
        print "Case #{}: {}".format(i, result)


if __name__ == "__main__":
    main()
