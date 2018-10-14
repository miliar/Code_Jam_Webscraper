import sys

chars = dict({'-': '+', '+': '-'})

def get_lines():
    return [line.rstrip('\n') for line in sys.stdin]

def flip_n(stack, num):
    result, length = '', len(stack)
    for index in range(0, min(num, length)):
        result += chars[stack[index]]
    return result + stack[min(num, length):length]

assert flip_n('+---', 3) == '-++-'
assert flip_n('----', 4) == '++++'
assert flip_n('+---', 1) == '----'

def happy(char, index=0):
    return char[index] == '+'

assert happy('+') == True
assert happy('-') == False
assert happy('++') == True

def unhappy_index_of(stack):
    for index in range(0, len(stack)):
        if not happy(stack, index):
            return index
    return -1

assert unhappy_index_of('+++') == -1
assert unhappy_index_of('++-') == 2
assert unhappy_index_of('-++') == 0

def happy_index_of(stack):
    for index in range(0, len(stack)):
        if happy(stack, index):
            return index
    return -1

assert happy_index_of('+++') == 0
assert happy_index_of('++-') == 0
assert happy_index_of('-++') == 1
assert happy_index_of('---') == -1

def cut_happy_tail(stack):
    if stack[0] == '+':
        unhappy_index = unhappy_index_of(stack)
        if unhappy_index == -1:
            return ''
        return stack[unhappy_index_of(stack):]
    return stack

assert cut_happy_tail('----+++') == '----+++'
assert cut_happy_tail('----++-') == '----++-'
assert cut_happy_tail('+++++') == ''

def solve(stack, num):
    if unhappy_index_of(stack) == -1:
        return 0
    total = 0
    while len(stack) > 0:
        stack = cut_happy_tail(stack)
        if len(stack) > 0:
            if len(stack) < num:
                return 'IMPOSSIBLE'
            stack = flip_n(stack, num)
            total += 1
    return total

assert solve('---+-++-', 3) == 3
assert solve('++++', 4) == 0
assert solve('-+-+-', 4) == 'IMPOSSIBLE'

lines = get_lines()
nb_cases = int(lines.pop(0))

for case in range(0, nb_cases):
    stack = lines.pop(0)
    infos = stack.split(' ')
    answer = solve(infos[0], int(infos[1]))
    print("Case #", (case + 1), ": ", answer, sep="")
