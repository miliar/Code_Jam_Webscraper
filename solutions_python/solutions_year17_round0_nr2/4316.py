#Google code jam TIDY

no_lines_str = input()
no_lines = int(no_lines_str)

count = no_lines

input_list = []

while count > 0:
    test_num_str = input()
    test_num = test_num_str
    input_list.append(test_num)

    count -= 1

ans_list = []
int_list = []
#print(input_list)

def tidycheck(b):
    blist = []
    big_check = 0
    for numb in b:
        blist.append(int(numb))
    num_length = len(blist)
    if num_length == 1:
        return True
    else:
        for j in range(num_length - 1):
            if blist[j] <= blist[j+1]:
                big_check += 0
            else:
                big_check += 1
        if big_check == 0:
            return True
        else:
            return False

for j in input_list:
    j_temp = j
    finder = False
    while finder ==  False:
        if tidycheck(j_temp) == True:
            ans_list.append(j_temp)
            finder = True
        else:
            k_temp = int(j_temp)
            k_temp -= 1
            j_temp = str(k_temp)

case_no = 1
for num in ans_list:
    print("Case #%i:" % case_no + " " + str(num) )
    case_no += 1
        
    
