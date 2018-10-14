# Google 2017 Code Jam, Charlie Crandall

# Take an integer and find the next lowest integer that is 'tidy'
def find_next(target):
    str_target = str(target)
    digit_count = len(str_target)
    digits = [int(x) for x in str_target]

# crawl the target's digits for untidyness
    for i in range(1, digit_count):
        if digits[i - 1] > digits[i]:
# next digit is too low, split the target, find a smaller, tidier, head
            head = find_next(int(str_target[:i]) - 1)
            tail = '9' * (digit_count - i)  # always maximum tidy
            return int(str(head)+str(tail))
    # If we made it this far, the number is already tidy
    return target

# Open the input file, process into code jam output format
with open('B-large.in') as f:
    for i, line in enumerate(f.readlines()[1:], start=1):
        number = int(line)
        output = find_next(number)
        print("Case #{}: {}".format(str(i), output))
