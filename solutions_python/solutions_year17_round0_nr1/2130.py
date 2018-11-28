def flip(stack, k):
    flips = 0
    if(len(stack) < k):
        return "IMPOSSIBLE"
    for i in range(len(stack)-(k-1)):
        if(stack == '+'*len(stack)):
            return flips
        if(stack[i] == '-'):
            for j in range(k):
                if(stack[i+j] == '+'):
                    stack = stack[:i+j] + '-' + stack[i+j+1:]
                else :
                    stack = stack[:i+j] + '+' + stack[i+j+1:]
            flips += 1
    if(stack == '+'*len(stack)):
        return flips
    else:
        return "IMPOSSIBLE"

if __name__ == '__main__':
    inp = open("large_input.txt", "r")
    out = open("large_output.txt","w")
    test_cases = [x.strip('\n') for x in inp.readlines()]
    test_case_num = 1
    while test_case_num <= int(test_cases[0]):
        index = test_cases[test_case_num].index(' ')
        stack = test_cases[test_case_num][0:index]
        flipper = int(test_cases[test_case_num][index+1:])
        flips = flip(stack, flipper)
        out.write('Case #{}: {}\n'.format(test_case_num,flips))
        test_case_num += 1

