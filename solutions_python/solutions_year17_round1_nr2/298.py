import sys
from math import ceil, floor


def load_info(f):
    line = f.readline().strip('\n')
    out = int(line)
    return out    

def my_function(f, case_num):
    print_info = []
    line = f.readline().strip('\n').split(' ')
    N, P = [int(x) for x in line]
    line = f.readline().strip('\n').split(' ')
    ingredients = [int(x) for x in line]
    packages = [[] for x in xrange(N)]
    for x in xrange(N):
        line = f.readline().strip('\n').split(' ')
        temp = [int(package) for package in line]
        temp.sort()
        
        diff = ingredients[x]*0.1
        l = ingredients[x] + diff
        u = ingredients[x] - diff
        for y in xrange(P):
            i = ceil(temp[y]/l)
            j = floor(temp[y]/u)
            packages[x].append(set([z for z in xrange(int(i),int(j)+1)]))
            
            

    kits = 0
    temp = packages[0]
    i = 1
    while i < N:
        temp1 = []
        j_o = 0
        for package in temp:
            j = j_o
            while j < P:
                temp2 = package & packages[i][j]
                if temp2:
                    
                    temp1.append(temp2)
                    
                    j_o = j+1
                    break
                j += 1
        temp = temp1
                
        i += 1
    res = 0
    for kit in temp:
        if kit:
            res += 1
    
            
    print 'case %d done' % (case_num+1)
    print_info.append('Case #' + str(case_num+1) + ': ' + str(res))
    
    print_info.append('\n')

    return print_info
    
if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Round 1A > ')
        input_args = str(raw_input())
        try:
            if input_args == 'exit':
                break
            elif input_args == '':
                continue
            else:
                args = input_args.split(' ')
                input_file = args[0]
                output_file = args[1]
        except:
            print('Invalid input. Please try again.')
        else:
            f_in = open(input_file)
            f_out = open(output_file, 'w')
            
            num_of_tests = load_info(f_in)
            try:
                for x in xrange(num_of_tests):
                    f_out.writelines(my_function(f_in, x))
##            except:
##                print('something wrong')
##            else:
##                print('File is built successfully!!!!')
##                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
