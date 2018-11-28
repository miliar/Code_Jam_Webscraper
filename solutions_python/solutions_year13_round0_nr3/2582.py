from math import sqrt

def read(filename):
    input = open(filename, 'r')
    lines = []
    for line in input:
        lines.append(line.rstrip('\n')) # strip out the newline characters
    return lines

def get_range(s):
    nums = list(map(int, s.split(' ')))
    return range(nums[0], nums[1] + 1)

def is_palindrome(num, is_sqrt):
    s = str(num)
    if is_sqrt:
        if s[-1:-3:-1] == '0.' and len(str(int(num))) + 2 == len(str(num)):
            s = s[:-2]
    return s == s[::-1]

def generate_squares(r):
    squares = []
    for i in r:
        if is_palindrome(i, False) and is_palindrome(sqrt(i), True):
            squares.append(i)
    return squares

def main():
    lines = read('C-small-attempt0.in')
    num = int(lines.pop(0))
    line_num = 0
    for i in range(num):
        total = len(generate_squares(get_range(lines[i])))
        print("Case #" + str(i + 1) + ": " + str(total))
        line_num += 1

if __name__ == '__main__':
    main()
