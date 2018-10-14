#! /usr/bin/python
import sys

def min_number(code):
    code_mapping = {code[0]: 1}
    number = [1]
    for i in range(1, len(code)):
        char = code[i]
        if code_mapping.has_key(char):
            number.append(code_mapping[char])
        else:
            if len(code_mapping) == 1:
                code_mapping[char] = 0
            else:
                code_mapping[char] = len(code_mapping)
            number.append(code_mapping[char])
    base = len(code_mapping)
    if base == 1:
        base = 2
    result = 0
    length = len(number)
    for i in range(length):
        result = result + number[i] * base ** (length - i - 1)
    return result

if __name__ == "__main__":
    input_file = sys.argv[1]
    ifile = open(input_file)
    case_count = int(ifile.readline().strip())
    for i in range(case_count):
        code = ifile.readline().strip()
        result = min_number(code)
        print "Case #%d: %d" % (i+1, result)
        