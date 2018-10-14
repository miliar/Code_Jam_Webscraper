import os
import math

infile_name = "B-large.in"
outfile_name = "B_output_large.txt"

def output(input_value, i):
    with open(outfile_name,'a') as outfile:
        outfile.write("Case #{0}: {1}\n".format(i, solve(input_value)))
        

def solve(input_value):
    digits = [int(x) for x in input_value]
    value = int(input_value)
    #digits = input_value
    prev = digits[0]
    for i, digit in enumerate(digits):
        if digit >= prev:
            prev = digit
        else:
            p10 = len(digits) - i
            value = value // 10**p10
            value *= 10**p10
            value -= 1
            value = solve(str(value))
            break
    return value
        
if __name__ == "__main__":
    if os.path.exists(outfile_name):
        os.remove(outfile_name)
    with open(infile_name, 'r') as infile:
        for i, line in enumerate(infile):
            if i > 0:
                output(line.strip(), i)