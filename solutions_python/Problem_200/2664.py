'''
Created on Apr 8, 2017

@author: khaled
'''

filename = 'B-large'
def main():
    in_file = open(filename+'.in', 'r')
    out_file = open(filename+'.out', 'w')
    
    lines = [l.rstrip('\n') for l in in_file.readlines()]
    
    T = int(lines[0])
    cases = lines[1:]
    
    for i in range(T):
        case = [x for x in cases[i]]
        
        for j in range(len(case)-1, 0, -1):
            if case[j] < case[j-1]:
                case[j:] = ['9' for x in range(j, len(case))]
                case[j-1] = '9' if case[j-1] == '0' else str(int(case[j-1]) - 1)
            
        first_positive = case.index(next(filter(lambda x: x != '0', case)))
        case = ''.join(case[first_positive:])                
   
        print('Case #{}: {}'.format(i+1, case), file=out_file)
        
        

if __name__ == '__main__':
    main()