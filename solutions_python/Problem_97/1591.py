T = int(raw_input())
for t in range(1, T+1):
    inp = raw_input()
    A, B = inp.split(' ')
    diff = int(A) - int(B)
    result = []
    result_int = 0
    for curr_num in range(int(A), int(B)+1):
        num_len = len(str(curr_num))
        changed_num = str(curr_num)
        for i in range(0, num_len):
            new_num = str(changed_num[num_len-1 : ]) + str( changed_num[ 0: num_len - 1 ] ) 
            if (int(new_num) > int(curr_num)) and (int(new_num) <= int(B)):
                pair = (int(curr_num), int(new_num))
                if (pair not in result):
                    result.append(pair)
                    result_int = result_int + 1
            changed_num = str(new_num)
    print "Case #%d: %d"%(t, result_int)
