def isTidy(num_str):
    cur = 0
    for digit in num_str:
        if (int(digit) < cur):
            return False
        cur = int(digit)
    return True

def startTidy(num_str):
    for i in range(1, len(num_str) + 1):
        if (not isTidy(num_str[:i])):
            return num_str[:i-1]
    return num_str

def largestTidyBefore(num_str):
    st = startTidy(num_str)
    if (st == num_str):
        return st
    return largestTidyBefore(str(int(st) - 1)) + ('9' * (len(num_str) - len(st)))

with open('input.txt', 'r') as input, open('out.txt', 'w') as out:
    num_cases = int(input.readline())
    for case in range(num_cases):
        num = input.readline().strip('\n\r')
        out.write('Case #' + str(case + 1) + ': ' + str(int(largestTidyBefore(num))) + '\n')
