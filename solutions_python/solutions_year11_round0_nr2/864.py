def do_calc(input):
    input = input.replace('\r','')
    input = input.split('\n')

    iters = int(input[0])
    
    results = ''
    
    for x in xrange(iters):
        line = input[x+1].split(' ',1)
        num_1 = int(line[0])
        line = line[1]
        
        combinations = {}
        for i in xrange(num_1):
            line = line.split(' ', 1)
            comb = line[0]
            combinations[comb[:2]] = comb[2]
            combinations[comb[1]+comb[0]] = comb[2]
            line = line[1]
        
        line = line.split(' ',1)
        num_2 = int(line[0])
        line = line[1]
        
        invokes = {}
        for i in xrange(num_2):
            line = line.split(' ', 1)
            invoke = line[0]
            line = line[1]
            
            i1 = invoke[0]
            i2 = invoke[1]
            
            if invokes.has_key(i1):
                if not i2 in invokes[i1]:
                    invokes[i1].append(i2)
            else:
                invokes[i1] = [i2]
                
            if invokes.has_key(i2):
                if not i1 in invokes[i2]:
                    invokes[i2].append(i1)
            else:
                invokes[i2] = [i1]
        
        line = line.split(' ',1)
        num_3 = int(line[0])
        line = line[1]
        
        elements = ''
        for i in xrange(num_3):
            elements += line[i]
            
            if len(elements) < 2:
                continue
            
            # check for combinations:
            sub_elem = elements[-2:]
            if combinations.has_key(sub_elem):
                elements = elements[:-2] + combinations[sub_elem]
            
            # check for kaboom!
            check = elements[-1]
            if invokes.has_key(check):
                bad_elems = invokes[check]
                for bad_elem in bad_elems:
                    if bad_elem in elements:
                        elements = ''
                        break
            
        results += ('Case #%i: [%s]\r\n' % (x+1, ', '.join(elements)))
    return results

def main():
    import os
    input_filename = os.path.abspath(__file__).split('.')[0] + '.in'
    output_filename = os.path.abspath(__file__).split('.')[0] + '.out'
    
    input_file = open(input_filename)
    input = input_file.read()
    input_file.close()
    results = do_calc(input)
    
    output_file = open(output_filename, 'w')
    output_file.write(results)
    output_file.close()
    

if __name__ == '__main__':
    main()