def is_tidy(num):
    for i in range(len(num)-1):
        if(int(num[-(i+1)]) < int(num[-(i+2)])):
            return False
    return True

def find_num(num):
    last_num = int(num)
    i = len(num) - 1
    pow = 1
    while(not is_tidy(num)):
        if(num[i] == '9') :
            i -= 1
            pow *= 10
        last_num -= pow
        num = str(last_num)
    return last_num



if __name__ == '__main__':
    inp = open("large_input.txt", "r")
    out = open("large_output.txt","w")
    test_cases = [x.strip('\n') for x in inp.readlines()]
    test_case_num = 1
    while test_case_num <= int(test_cases[0]):
        last_num = test_cases[test_case_num]
        last_tidy_num = find_num(last_num)
        out.write('Case #{}: {}\n'.format(test_case_num,last_tidy_num))
        test_case_num += 1
