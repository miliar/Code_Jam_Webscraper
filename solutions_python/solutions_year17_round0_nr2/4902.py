from collections import deque

def lastTidy(input):
    while input > 0:
        if not isTidy(input):
            input = input - 1
        else:
            return input

def isTidy(num):
    numArray = magic(num) # get list of ints
    
    previous = numArray[0]
    for number in numArray:
        if number < previous:
            return False
        previous = number
    return True

def magic(num):
    digits = deque()
    while True:
        num, r = divmod(num, 10)
        digits.appendleft(r)
        if num == 0:
            break
    return list(digits)


with open('input') as f:
    inputs = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
inputs = [x.strip() for x in inputs]
inputs.pop(0)

cases = len(inputs)
solutions = []

for input in inputs:
    solutions.append(lastTidy(int(input)))

x = 1
y = 0
while x <= cases:
    with open('output', 'a') as the_file:
        the_file.write('Case #'+str(x)+': ' +str(solutions[y]) + '\n')
    x=x+1
    y=y+1

