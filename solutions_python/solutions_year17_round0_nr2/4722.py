def tidy_number(n):
    for num in range(n,0,-1):
        str_num = str(num)
        if len(str_num) > 1:
            for i in range(0,len(str_num)-1):
                if int(str_num[i]) > int(str_num[i+1]):
                    break;
                if i == len(str_num)-2:
                    return num
        else:
            return num
    return


total_cases=int(input())
for num_case in range(1,total_cases+1):
    n = int(input())
    print("Case #{}: {}".format(num_case,tidy_number(n)))
