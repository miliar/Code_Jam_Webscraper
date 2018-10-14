import sys, math

input_file=None
output_file=open("output.txt", 'w')

def isPalimdrome(num):
    num_str = str(num)
    reverse_num = num_str[::-1]
    return num_str == reverse_num

def main():
    input_file=open(sys.argv[1], 'r')
    number_of_test_cases = int(input_file.readline())
    for k in range (0,number_of_test_cases):
        limits_list = (input_file.readline()).split()
        lower_limit = long(math.ceil(math.sqrt(long(limits_list[0]))))
        upper_limit = long(math.sqrt(long(limits_list[1])))
        num_palindromes = 0
        for i in range(lower_limit, upper_limit+1):
            if isPalimdrome(i):
                if isPalimdrome(i*i):
                    num_palindromes += 1
        output_file.write("Case #%d: %d\n" %(k+1, num_palindromes))
    return

main()