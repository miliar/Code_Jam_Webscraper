lines = [line.rstrip('\n') for line in open('C-small-1-attempt0.in')]

T = int(lines[0])
str_temp = ''

def generate(N,K):    
    n_plus_2 = [1]+[0 for x in range(N)]
    n_plus_2.append(1)
    
    for k in range(K):

        l_s_dict = {}
        r_s_dict = {}

        for index in range(len(n_plus_2)):

            if n_plus_2[index] == 1:
                pass
            else:
                left_arr = n_plus_2[:index]
                left_arr = left_arr[::-1]
                right_arr = n_plus_2[index+1:]

                l_s = left_arr.index(1)
                r_s = right_arr.index(1)

                l_s_dict[index] = l_s
                r_s_dict[index] = r_s

        min_l_r_dict = {}

        for key in l_s_dict:
            l = l_s_dict[key]
            r = r_s_dict[key]

            min_l_r_dict[key] = min(l,r)

        _min_val = max(min_l_r_dict.values())
        _min_keys = [k for k, v in min_l_r_dict.items() if v == _min_val]

        #Not single key
        if len(_min_keys) != 1:

            max_l_r_dict = {}
            for key in _min_keys:
                l = l_s_dict[key]
                r = r_s_dict[key]

                max_l_r_dict[key] = max(l,r)

            _max_val = max(max_l_r_dict.values())
            _max_keys = [k for k, v in max_l_r_dict.items() if v == _max_val]

            if len(_max_keys) != 1:
                _max_keys.sort()
                sweet_index = _max_keys[0]
            else:
                sweet_index = _max_keys[0]
        else:
            sweet_index = _min_keys[0]
            
        n_plus_2[sweet_index] = 1
        
        if k+1 == K:
            final_max_l_r = max(l_s_dict[sweet_index],r_s_dict[sweet_index])
            final_min_l_r = min(l_s_dict[sweet_index],r_s_dict[sweet_index])
            
            return str(final_max_l_r)+' '+str(final_min_l_r)

for t in range(1,T+1):
    main_str = lines[t]
    N = int(main_str.split(' ')[0])
    K = int(main_str.split(' ')[1])
    print(t)

    if t == T:
        str_temp = str_temp+'Case #'+str(t)+': '+str(generate(N,K))
    else:
        str_temp = str_temp+'Case #'+str(t)+': '+str(generate(N,K))+'\n'
        
print(str_temp)
f = open('out.txt', 'w')
f.write(str_temp)
f.close()            