def solve(string, flips):
    stack = list(string)
    num_flips = 0
    for idx, x in enumerate(stack):
        if x == '-':
            flip(idx, flips, stack)
            num_flips += 1
    if not is_it_posible(stack, flips):
        return 'IMPOSSIBLE'
    return str(num_flips)

def flip(where, spaces, stack):
    for x in range(spaces):
        if where + spaces - 1 < len(stack):
            if stack[where + x] == '-':
                stack[where + x] = '+'
            else:
                stack[where + x] = '-'
        else:
            break
    return stack

def is_it_posible(stack, flips):
    count = 0
    for x in stack:
        if x == '-':
            count += 1
    if count == 0:
        return True
    return count >= flips

file = open('A-small-attempt0.in')
output = open('answer-small.txt','w')
cases = int(file.readline())  # read a line with a single integer
for i in range(1, cases + 1):
    input = file.readline().strip().split()
    if i == 4:
        pass
    output.write('Case #'+str(i)+': '+solve(input[0], int(input[1]))+'\n')
output.close()