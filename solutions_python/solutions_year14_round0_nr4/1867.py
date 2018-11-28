# Test

import bisect
import random

def war_score(arr_1, arr_2):
    """
    calculate the war game score
    """

    final_score = 0 ; 
    
    while len(arr_1) > 0 :

        N = len(arr_1) ; 
        index =  0 ;
        
        item = arr_1[index] ;

        # too big, no one can beat
        if item > arr_2[-1] :
            final_score = final_score + 1 ;
            del arr_1[index] ;
            del arr_2[0] ;
            
        else : 
            index_2 = bisect.bisect_left(arr_2, item) ;

            del arr_1[index] ;
            del arr_2[index_2] ;

    return final_score ; 

def cheat_war(arr_1, arr_2, record_map):
    """
    cheat war, DP version
    """

    temp_list = arr_1 + arr_2 ; 
    key = tuple(temp_list) ;
    
    #print(key)
    
    if key in record_map :
        return record_map[key], record_map ; 

    else :
        # If only one length
        if len(arr_1) == 1 :
            if arr_1[0] > arr_2[0] :
                record_map[key] = 1 ; 
            else :
                record_map[key] = 0 ; 

            return record_map[key], record_map ;

        # More than one.. solve it by DP
        # Case 1: pretend to lose
        new_arr_1 = list(arr_1) ;
        new_arr_2 = list(arr_2) ;

            
        del new_arr_1[0] ;
        del new_arr_2[-1] ;

        val_1, map_1 = cheat_war(new_arr_1, new_arr_2, record_map) ;

        # Case 2: Try to Eat the one
        new_arr_1 = list(arr_1) ;
        new_arr_2 = list(arr_2) ;

        item = new_arr_2[0] ; 
        index = bisect.bisect_left(new_arr_1, item) ;

        if index < len(new_arr_1) :
            del new_arr_1[index] ;
            award = 1 ; 
        else :
            del new_arr_1[0] ;
            award = 0 ;
            
        del new_arr_2[0] 
        val_2, map_2 = cheat_war(new_arr_1, new_arr_2, record_map) ; 

        # DP decision
        if arr_1[0] < arr_2[-1] :
            flag_1 = 1 ;
        else :
            flag_1 = 0 ;

        #if arr_2[0] < arr_1[-1] :
        flag_2 = 1 ;
        #else :
            #flag_2 = 0 ;

        record_map[key] = max(flag_1* val_1, award + flag_2* val_2) ; 

        return record_map[key], record_map ; 
    
#f = open('sample_input.txt', 'r') ;
f = open('test', 'r') ;
f_write = open('result','w')

row = f.readlines() ;

num_case = int(row[0]) ;
#print('NUM', num_case)

for case_index in range(0, num_case) :
    case_num = int(row[case_index*3 + 1]) ;
    #case_2_row = int(row[index*10 + 6]) ;  

    line_1_use = row[case_index*3 + 2] ;
    line_2_use = row[case_index*3 + 3] ;

    # parse the element
    info_1 = [float(x) for x in line_1_use.split()]
    info_2 = [float(x) for x in line_2_use.split()]

    # Sort result 
    info_1.sort() ; 
    info_2.sort() ; 

    # cheat score
    use_arr_1 = list(info_1)
    use_arr_2 = list(info_2)
    my_map = dict() ; 

    print(type(my_map)) ;
    
    Cheat_war, my_map =  cheat_war(use_arr_1, use_arr_2, my_map)

    # War score
    
    use_arr_1 = list(info_1)
    use_arr_2 = list(info_2)
    
    Naomi_war =  war_score(use_arr_1, use_arr_2)

    pre_out = "Case #" + str(case_index +1) + ": " + str(Cheat_war) +  " " + str(Naomi_war) + '\n'
    #print(pre_out, final_str)
    f_write.write(pre_out)


'''
    result_set = set_1.intersection(set_2) ; 

    if len(result_set) >1 :
        final_str = "Bad magician!"

    if len(result_set) == 0 :
        final_str = "Volunteer cheated!"
        
    if len(result_set) == 1 :
        final_str = result_set.pop() ;
'''


