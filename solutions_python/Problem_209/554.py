import sys
from math import pi


def load_info(f):
    line = f.readline()
    out = int(line)
    return out    

def my_function(f, case_num):
    print_info = []
    line = f.readline()
    N, K = [int(x) for x in line.strip('\n').split(' ')]
    pancakes = []
    for x in xrange(N):
        R, H = [int(x) for x in f.readline().strip('\n').split(' ')]
        pancakes.append([R,H,R*H])
    pancakes.sort(key = lambda p:-p[2])
    i = 0
    max_R = 0
    res1 = 0
    while i < K-1:
        res1 += pancakes[i][2]
        if pancakes[i][0] > max_R:
            max_R = pancakes[i][0]
        i += 1
    res2 = 0
    temp_R2 = max_R**2
    while i < N:
        if pancakes[i][0] > max_R:
            temp = pancakes[i][0]**2 + 2*pancakes[i][2]
        else:
            temp = temp_R2 + 2*pancakes[i][2]
        if temp > res2:
            res2 = temp
        i += 1
    
    res = pi * (2*res1 + res2)
    print_info.append('Case #%d: %.7f' % (case_num+1, res))
    print_info.append('\n')

    return print_info
    
if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('2017 R1C_1 > ')
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
