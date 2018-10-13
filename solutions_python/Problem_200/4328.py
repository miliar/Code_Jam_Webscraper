t = int(input())

def is_tidy(n):
    n_str = str(n)
    
    for i in range(1, len(n_str)):
        # print(n_str[i- 1], n_str[i])
        if (n_str[i- 1] > n_str[i]):
            return i-1
    return -1


for k in range(1, t + 1):
    n = int(input())
    tidy_num_index = is_tidy(n)
    n_str = str(n)
    if(tidy_num_index != -1):
        tidy_num_str = n_str[0:tidy_num_index]
        tidy_num_str += str(int(n_str[tidy_num_index]) - 1)
        if (int(n_str[0]) > int(n_str[tidy_num_index+1]) and int(n_str[0]) >= int(n_str[tidy_num_index])  ): 
            string = ""
            if int(n_str[0]) == 0:
                string += '9'
            else:
                string += str(int(n_str[0]) - 1)
            for i in range(1,tidy_num_index + 1):
                string += '9'
            tidy_num_str = string
        for i in range(tidy_num_index+1, len(n_str)):
            tidy_num_str += '9'
        n = int(tidy_num_str)
    # while(tidy_num_index != -1):
    #     n_str = str(n)
    #     for i in range(tidy_num_index, len(n_str)):
    #         n_str[i] = '9'
    #     n = int(n_str)
    #     tidy_num_index = is_tidy(n)
    print("Case #{}: {}".format(k, n))

