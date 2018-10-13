def tidy_numbers(n):
    #digits in n are same; return n
    if len({dig for dig in str(n)})==1:
        return n
    digits = [int(dig) for dig in str(n)]
    index = len(digits)-1
    while index:
        #compare each consecutive pair
        #if untidy, make it tidy
        if digits[index] < digits[index-1]:
            digits[index:] = [9 for i in range(len(digits[index:]))]
            digits[index-1] -= 1
        index-=1
    return int(''.join(str(dig) for dig in digits))
    

def input_output():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        print("Case #{}: {}".format(i, tidy_numbers(n)))
        # check out .format's specification for more formatting options

if __name__ == "__main__":
    input_output()
