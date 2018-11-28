import math

def palindrome(num):
    return str(num) == str(num)[::-1]

def count_palindrome(input_range):
    # Define initial count
    initial_count = 0
    input_range = input_range.split()
    first_num = input_range[0]
    second_num = input_range[1]
    for num in range(int(first_num), int(second_num)+1):
        #get the reverse and check if number is palindrome.
        # if number starts with 0, skip it.
        if str(num).startswith('0'):
            pass
        else:
            rev_num = palindrome(num)
            #print rev_num, num
            #print num

            if rev_num:
                # check if square root is palindrome.
                sqrt_num = math.sqrt(num)
                #print sqrt_num
                # get the real and imaginary part of sqrt
                sqrt_num = str(sqrt_num).split('.')
                
                if sqrt_num[1] == '0':
                    rev_sqrt_num = palindrome(sqrt_num[0])

                    if rev_sqrt_num:
                        initial_count = initial_count + 1

    return initial_count

if __name__=="__main__":
    # read the input file and get the values.
    i = 0
    with open('C-small-attempt0.in') as file_input:
        next(file_input)
        for line in file_input:
            line = line.strip('\n')
            print line
            i = i + 1
            count = count_palindrome(line)
            print "count is "+str(count)

            file_out = open('output.txt', 'a')
            file_out.writelines('Case #%s: %s\n' % (str(i), str(count)))
      
