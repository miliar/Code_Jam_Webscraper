def handle_input(file):
    input_list = file.readlines()
    cases = int(input_list[0])
    for i in range(1, cases + 1, 1):
        current_num = input_list[i].rstrip('\n')
        print('Case #' + str(i) + ': ' + str(handle_num(current_num)))

def handle_num(num: str):
    if check_tidy(num):
        return num
    
    pointer = len(num) - 1
    
    for i in range(len(num)):
        base_num = num[:pointer]
        temp_num = num
        for j in range(int(num[pointer]) - 1, -2, -1):
            if j == -1:
                num = base_num + '9'
                pointer -= 1
            else:
                temp_num = base_num + str(j) + '9' * i
                if check_tidy(temp_num):
                    temp_num = temp_num.lstrip('0')
                    return temp_num
     
                    
def check_tidy(num: str):
    for i in range(0, len(num) - 1, 1):
        if num[i] > num[i+1]:
            return False
    return True

handle_input(open('B-large.in', 'r'))

