import math

def is_square_and_res_is_palindrome(n):
    res = math.sqrt(n)
    return res.is_integer() and is_palindrome(int(res))

def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

with open('C-small-attempt0.in') as input_data:
    output_data = open('C.out', 'w')
    t = int(input_data.readline())
    cases = []
    for i in range(t):
        a, b = map(int, input_data.readline().rstrip().split())
        num = 0
        for x in range(a, b+1):
            if is_square_and_res_is_palindrome(x) and is_palindrome(x):
                num += 1
                print(x)
        output_data.write("Case #%d: %d\n" % (i+1, num))
    output_data.close()
