INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'B-large.out'

def read_input():
    f = open(INPUT_FILE, 'r')
    num_test_cases = int(f.readline())
    
    for i in range(num_test_cases):
        yield f.readline().split()
        
    f.close()

def write_output(outputs):
    f = open(OUTPUT_FILE, 'w')
    f.write('\n'.join(outputs))
    f.write('\n')
    f.close()

if __name__ == '__main__':
    outputs = []
    for case in read_input():
        # Setup
        num_combinations = int(case[0])
        combinations = {}
        for combination in case[1:1 + num_combinations]:
            combinations[combination[:2]] = combination[2]
            
        num_oppositions = int(case[num_combinations + 1])
        oppositions = case[num_combinations + 2:num_combinations + 2 + num_oppositions]
        
        element_invokation_order = case[-1]
        
        # Calculation
        element_list = []
        for element in element_invokation_order:
            element_list.append(element)
            pair = ''.join(element_list[-2:])
            if len(pair) == 2:
                # Try and combine the last two elements
                new_element = combinations.get(pair) or combinations.get(pair[::-1])
                if new_element is not None:
                    element_list = element_list[:-2]
                    element_list.append(new_element)
                
                # Watch out for opposing elements
                for opposition in oppositions:
                    if opposition[0] in element_list \
                    and opposition[1] in element_list:
                        element_list = []
                    
        outputs.append('Case #%d: [%s]' % (len(outputs)+1, ', '.join(element_list)))
    
    write_output(outputs)