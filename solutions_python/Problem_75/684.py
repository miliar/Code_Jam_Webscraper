'''
Created on 06/05/2011

@author: Shimi
'''

import sys
from test.test_iterlen import len

OUTPUT_FILEPATH = 'output_file_magicka'

def compute_final_element_list(case_line):
    case_line_arr = case_line.split()
    
    # create combinations list
    num_of_combs = int(case_line_arr[0])
    combs_list = case_line_arr[1:num_of_combs + 1]
    combs_dict = {}
    
    for comb in combs_list:
        combs_dict[comb[:2]] = comb[2]
        combs_dict[comb[1] + comb[0]] = comb[2]
     
    # create oppositions list
    num_of_oppos = int(case_line_arr[num_of_combs + 1])
    first_opp_index = num_of_combs + 2
    oppos_list = case_line_arr[first_opp_index: first_opp_index + num_of_oppos]
    oppos_list = oppos_list + [opp[1] + opp[0] for opp in oppos_list]
    
    # create element list
#    num_of_elements = int(case_line_arr[first_opp_index + num_of_oppos])
    elements_str = case_line_arr[first_opp_index + num_of_oppos + 1]
    elements_list = []
    last_elem_index = -1
    
    for elem in elements_str:
        if last_elem_index >= 0:
            cur_comb = elements_list[last_elem_index] + elem
            if combs_dict.has_key(cur_comb):
                elements_list[last_elem_index] = combs_dict[cur_comb]
            else:
                for elem_in_list in elements_list:
                    if elem + elem_in_list in oppos_list:
                        elements_list = []
                        last_elem_index = -1
                        break
                if len(elements_list) == 0:
                    continue
                else:
                    elements_list.append(elem)
                    last_elem_index += 1
        else:
            elements_list.append(elem)
            last_elem_index += 1
            
    return elements_list
        
def main():
    filepath = sys.argv[1]
    input_file = open(filepath, "rb")
    output_file = open(OUTPUT_FILEPATH, "wb")
    lines = input_file.readlines()[1:]
    input_file.close()
    
    for i, line in enumerate(lines):
        output_file.write("Case #%d: [" % (i + 1));
        final_elems_ls = compute_final_element_list(line)
        if len(final_elems_ls) > 0: 
            for elem in final_elems_ls[:-1]:
                output_file.write("%s, " % (elem))
            output_file.write("%s]\n" % (final_elems_ls[-1]))
        else:
            output_file.write("]\n")
    
    output_file.close()
    return
        
if __name__ == "__main__":
    main()