'''
Code Jam 2017
Problem A. Oversized Pancake Flipper
'''
UP_CHAR = '+'
DOWN_CHAR = '-'
T = int(input())  # read a line with a single integer
def flip_the_cake(cake):
    '''
    Flip a cake - >> + and + >> -
    '''
    if cake == DOWN_CHAR:
        return UP_CHAR
    return DOWN_CHAR
def do_the_test(pan, flipper):
    '''
    From the begin to the end, if you see any DOWN_CHAR, flip it
    '''
    stack = list(pan)
    index = 0
    count = 0
    while index + flipper < len(pan):
        if stack[index] == DOWN_CHAR:
            for j in range(index, index + flipper):
                stack[j] = flip_the_cake(stack[j])
            count += 1
        index += 1
    for j in range(index + 1, len(pan)):
        if stack[j] != stack[index]:
            return 'IMPOSSIBLE'
    if stack[index] == UP_CHAR:
        return count
    return count + 1
for i in range(1, T + 1):
    data = input().split(" ")
    test = data[0]
    tool = int(data[1])
    result = do_the_test(test, tool)
    print("Case #{}: {}".format(i, result))
