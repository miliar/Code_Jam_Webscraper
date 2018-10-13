import re

sre = re.compile(r'(?P<bot>\S)\s(?P<button>\d{1,3})')

def do_calc(input):
    input = input.replace('\r','')
    input = input.split('\n')

    iters = int(input[0])
    
    results = ''
    
    for x in xrange(iters):
        line = input[x+1]

        taken = 0
        places = {
            'O': 1,
            'B': 1,
        }

        all_moves = sre.findall(line)
        o_moves = [j for i,j in all_moves if i=='O']
        b_moves = [j for i,j in all_moves if i=='B']
        
        for bot,button in all_moves:
            temp_taken = abs(int(button)-places[bot])+1
            places[bot] = int(button)
            
            taken += temp_taken
            
            if bot == 'O':
                o_moves.pop(0)
            else:
                b_moves.pop(0)
            
            if bot == 'O':
                try:
                    other_next = int(b_moves[0])
                except IndexError:
                    continue
                cur = places['B']
                diff = abs(other_next -cur)
                if temp_taken >= diff:
                    places['B'] = other_next
                else:
                    if other_next > cur:
                        places['B'] += temp_taken
                    else:
                        places['B'] -= temp_taken
            else:
                try:
                    other_next = int(o_moves[0])
                except IndexError:
                    continue
                cur = places['O']
                diff = abs(other_next -cur)
                if temp_taken >= diff:
                    places['O'] = other_next
                else:
                    if other_next > cur:
                        places['O'] += temp_taken
                    else:
                        places['O'] -= temp_taken

        results += ('Case #%i: %i\r\n' % (x+1, taken))
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