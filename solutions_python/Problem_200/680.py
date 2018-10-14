'''
Code Jam 2017
Problem B. Tidy Numbers
'''
T = int(input())  # read a line with a single integer
def make_tidy(num):
    '''
    Make the tidy number according to the rule
    '''
    text = str(num)
    stack = list(text)
    #convert to number
    for index in range(0, len(stack)):
        stack[index] = int(stack[index])
    size = len(stack)
    index = size - 1
    while index >= 1:
        if stack[index] < stack[index - 1]:
            tmp = index - 1
            while stack[tmp] == 0:
                stack[tmp] = 9
                tmp -= 1
            stack[tmp] -= 1
            for j in range(index, size):
                stack[j] = 9
        index -= 1
    if stack[0] == 0:
        stack = stack[1:]
    return ''.join(map(str, stack))

for i in range(1, T + 1):
    test = int(input())
    result = make_tidy(test)
    print("Case #{}: {}".format(i, result))
