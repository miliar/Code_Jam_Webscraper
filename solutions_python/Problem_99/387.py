CASE_SIZE = 2



def main():
    with open('input.txt') as f:        
        all_lines = f.readlines()
        
    num_cases = int(all_lines[0])
    result = []
    for case_nbr in xrange(num_cases):
        
        num_chars_typed, num_chars_in_pword = all_lines[case_nbr*CASE_SIZE+1].strip().split(" ")
        num_chars_typed = int(num_chars_typed)
        num_chars_in_pword = int(num_chars_in_pword)
        probabilities = [float(x) for x in all_lines[case_nbr*CASE_SIZE+2].strip().split(" ")]
        
        
        expected_quit = 2 + num_chars_in_pword
        
        options = {(True,):probabilities[0], 
                   (False,):1-probabilities[0], 
                   }
        for p in probabilities[1:]:
            for key in options.keys()[:]:
                value = options.pop(key)
                new_key_true = tuple(list(key) + [True])
                new_key_false = tuple(list(key) + [False])
                options[new_key_true] = value * p
                options[new_key_false] = value * (1-p)
        values = {}
        
        for i in range(num_chars_typed+1):
            values[i] = 0
        
        for key, p in options.iteritems():
            for d in values.keys()[:]:
                ok = True
                for i, x in enumerate(list(key)[::-1]):
                    if not x and i+1 >= d: #failed
                        ok = False
#                print d, key, ok, i
                if not ok:
                    values[d] += p * (num_chars_in_pword*2 - num_chars_typed +2 + d)
                else:
                    values[d] += p * (num_chars_in_pword - num_chars_typed +1 + d)
#            print values
        all_values = values.values() + [expected_quit]
        
        result.append( "Case #%s: %s \n" % (case_nbr+1, min(all_values)))
    for r in result:
        print r
#    
    with open('output.txt','w') as f:        
        all_lines = f.writelines(result)

main()
print "done"
