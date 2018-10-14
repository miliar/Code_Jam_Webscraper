# developped under python3.2
test_file_name = 'B-large'
f = open(test_file_name + '.in', 'r')
fw = open(test_file_name + '.out', 'w')
T = int(f.readline())
for case in range(1,T+1):
    #print(i)
    
    line = f.readline()
    line = line.split()
    line.reverse()

    combine_in_1, combine_in_2, combine_out = [], [], []
    opposition_1, opposition_2 = [], []
    
    # read data
    C = int(line.pop())
    for item_c in range(0, C):
        string_c = line.pop()
        combine_in_1.append( string_c[0] )
        combine_in_2.append( string_c[1] )
        combine_out.append( string_c[2] )
        # both of the two sense are needed.
        combine_in_1.append( string_c[1] )
        combine_in_2.append( string_c[0] )
        combine_out.append( string_c[2] )        
    D = int(line.pop())
    for item_d in range(0, D):
        string_d = line.pop()
        opposition_1.append( string_d[0] )
        opposition_2.append( string_d[1] )
        opposition_1.append( string_d[1] )
        opposition_2.append( string_d[0] )        

    N = int(line.pop())
    # check the \n
    string_list = list(line.pop())
    string_list.reverse()
    # end read data

    # data process
    ans = []
    for item_n in range(0, N):
        is_has_combine = False
        is_has_opposite = False
        
        c = string_list.pop()
        if( len(ans) == 0 ):
            ans.append( c )
            continue
        for i in range(0, len(combine_in_1)):
            if( c == combine_in_2[i] and
                ans[-1] == combine_in_1[i]):
                ans.pop()
                ans.append( combine_out[i] )
                is_has_combine = True
                continue
        if( not is_has_combine ):
            for i in range(0, len(opposition_1)):
                if( c == opposition_2[i] and
                    ans.count( opposition_1[i] ) > 0):
                    ans = []
                    is_has_opposite = True
                    continue
        # attention: len(ans)>1!!
        if( len(ans) > 0 and not is_has_combine and not is_has_opposite ):
            ans.append( c )

    # end data process

    # result representation
    
    #print(ans)
    str_ans = ""
    for char in ans:
        str_ans += char + ', '
    if( len(str_ans)>2 and str_ans[-2] == ',' and str_ans[-1] == ' ' ):
        str_ans = str_ans[0:-2]
    output = 'Case #' + str(case) +': [' + str_ans + ']'
    print(output)

    fw.write(output + '\n')

    # end result representation

f.close()
fw.close()
