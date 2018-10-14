def is_tidy(number):
    prev_digit = number % 10;
    while number != 0:
        number /= 10
        digit = number % 10
        if digit > prev_digit:
            return False
        prev_digit = digit
    return True

if __name__ == '__main__':
    with open('B-small-attempt1.in', 'r') as file:
        line_no = 0
        for line in file:
            if line_no == 0:
                line_no += 1
                continue
            number = long(line)
            for i in range(number, -1, -1):
                if is_tidy(i):
                    print("Case #" + str(line_no) + ": " + str(i))
                    break
            line_no += 1
        
