testCases = int(input())

for case in range(0, testCases):
    inputs = input().split()
    stack = list(inputs[0])
    flipper = int(inputs[1])
    turns = 0
    impos = False
    while '-' in stack:
        bottom = ''.join(stack).rfind('-')
        if bottom - (flipper - 1) < 0:
            impos = True
            break
        for i in range(bottom - (flipper - 1), bottom + 1):
            if stack[i] == '-':
                stack[i] = '+'
            elif stack[i] == '+':
                stack[i] = '-'
        turns += 1
    if impos:
        print('Case #{}: IMPOSSIBLE'.format(case + 1))
    else:
        print('Case #{}: {}'.format(case + 1, turns))
