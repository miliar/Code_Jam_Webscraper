'''
Created on May 7, 2011

@author: karnr
'''
from collections import namedtuple

Input = namedtuple("Input", ('combine_list', 'destroy_list', 'element_list'))

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        test_input = fh.readline().strip().split()
        
        index = 0
        num_of_combines = int(test_input[index])
        index += 1
        
        start_idx = index
        index += num_of_combines
        end_idx = index
        combine_list = [list(str(s)) for s in test_input[start_idx:end_idx]]
        
        num_of_destroy = int(test_input[index])
        index += 1
        
        start_idx = index
        index += num_of_destroy
        end_idx = index
        destroy_list = [list(str(s)) for s in test_input[start_idx:end_idx]]
        
        num_of_elements = int(test_input[index])
        element_list = list(str(test_input[index + 1]))
        assert len(element_list) == num_of_elements
        
        test_data[count] = Input(combine_list, destroy_list, element_list)
        count += 1
        
    fh.close()
    return test_data

def _execute_test(test_input):
    combine_map = dict() 
    for (a,b,c) in test_input.combine_list:
        combine_map[(a, b)] = c
        combine_map[(b, a)] = c
        
    destroy_map = dict() 
    for (a,b) in test_input.destroy_list:
        if a not in destroy_map:
            destroy_map[a] = set()
            
        destroy_map[a].add(b)
        
        if b not in destroy_map:
            destroy_map[b] = set()
            
        destroy_map[b].add(a)
        
    final_list = list()
    
    for e in test_input.element_list:
        try:
            top = final_list[-1]
            ce = combine_map.get((e, top), None)
            if ce is not None:
                final_list.pop()
                final_list.append(ce)  
                continue
            
            destroy_set = destroy_map.get(e, None)
            if destroy_set is not None:
                count = sum([final_list.count(x) for x in destroy_set])
                if count > 0:
                    final_list = list()
                    continue  
            
        except IndexError:
            pass
        
        final_list.append(e)
    
    return "[%s]" % ", ".join(final_list)

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))
        
    output.close()
    
if __name__ == '__main__':
    main()