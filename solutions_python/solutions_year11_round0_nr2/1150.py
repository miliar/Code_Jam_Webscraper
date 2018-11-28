with open('magicka.in') as f:
    cases = int(f.readline())
    current_case = 1
    while current_case <= cases:
        case_data = f.readline().split(" ")
        combinations = {}
        opposed = {}
        final_invoke = []
        
        combination_count = int(case_data.pop(0))
        i = 0
        while i < combination_count:
            combo_set = case_data.pop(0)
            combinations[combo_set[0:2]] = combo_set[2]
            i += 1
        
        opposed_count = int(case_data.pop(0))
        i = 0

        while i < opposed_count:
            opposed_set = case_data.pop(0)
            opposed[opposed_set[0]] = opposed_set[1]
            opposed[opposed_set[1]] = opposed_set[0]
            i += 1
        
        invoke_count = int(case_data.pop(0))
        invoke_set = case_data.pop(0).strip()

        while len(invoke_set):
            
            final_invoke.append(invoke_set[0])
            invoke_set = invoke_set[1:]
            
            if len(final_invoke) > 1:
                current_pair = ''.join(final_invoke[-2:])
                for k, v in combinations.iteritems():
                    if current_pair == k or current_pair[::-1] == k:
                        final_invoke = final_invoke[:-2]
                        final_invoke.append(v)
                        break
                    
            if opposed.get(final_invoke[-1], None) in final_invoke:
                final_invoke = []
                    
        print("Case #%d: [%s]" % (current_case, ', '.join(final_invoke)))
        current_case += 1
            

        
        
                
            
                
        
        