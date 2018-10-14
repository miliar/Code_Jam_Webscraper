'''
Created on Apr 8, 2017

@author: khaled
'''

import re

filename = 'A-large'
def main():
    in_file = open(filename+'.in', 'r')
    out_file = open(filename+'.out', 'w')
    
    lines = [l.rstrip('\n') for l in in_file.readlines()]
    
    T = int(lines[0])
    cases = lines[1:]
    
    for i in range(T):
        case = cases[i]
        row_pancakes, flipper_length = case.split(' ')
        flipper_length = int(flipper_length)
        row_stripped = row_pancakes[:]
        flips = 0
        
        while True:
            
            row_stripped = row_stripped.lstrip('+').rstrip('+')
            
            first_minus = row_stripped.find('-')
            if first_minus == -1:
                break
            
            if len(row_stripped) >= flipper_length:
                sub_row = []
                for j in range(0, flipper_length):
                    if row_stripped[j] == '-':
                        sub_row.append('+')
                    else:
                        sub_row.append('-')
                        
                row_stripped = ''.join(sub_row) + row_stripped[flipper_length:]
            else:
                flips = -1
                break
                            
#             if re.search('-\+-', row_stripped):
#                 flips = -1
#                 break
                    
            flips += 1
            
        if flips >= 0:    
            print('Case #{}: {}'.format(i+1, flips), file=out_file)
        else:
            print('Case #{}: {}'.format(i+1, 'IMPOSSIBLE'), file=out_file)
        
        

if __name__ == '__main__':
    main()