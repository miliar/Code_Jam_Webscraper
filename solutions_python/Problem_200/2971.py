import sys 
sys.stdin.readline()
linenum = 1
def tidy(number):
    if number < 10:
        return number 
    tempnum = number
    i = 0
    while tempnum >= 100:
        tempnum //= 10
        i += 1
    if tempnum % 10 < tempnum // 10:
        return (tempnum // 10) *  pow(10, (i + 1)) - 1
    return (tempnum // 10) * pow(10, (i + 1)) + tidy(number % (pow(10, (i+1))))
    
def istidy(number):
    if number < 10:
        return True
    if number % 10 < (number // 10) % 10:
        return False 
    return istidy(number // 10)
    
for line in sys.stdin:
    print('Case #%d: ' % linenum, end = '')
    linenum += 1
    number = int(line)
    while not istidy(number):
        number = tidy(number)
    if line[-1] == '\n':
        print(number)
    else:
        print(number, end = '')

