import sys


def load_info(f):
    line = f.readline()
    out = int(line)
    return out    

def my_function(f, case_num):
    print_info = []
    line = f.readline().strip('\n')
    N = [int(x) for x in line]
    n = len(N)
    i = n-1
    
    while i > 0:
        
        if N[i] < N[i-1]:
            N[i-1] -= 1
            for i in xrange(i,n):
                N[i] = 9
        i -= 1
    res = ''
    leading_zero = True
    
    for d in N:
        if leading_zero and not d:
            continue
        elif leading_zero and d:
            leading_zero = False
        res += str(d)
        
    print_info.append('Case #' + str(case_num+1) + ': ' + res)
    print_info.append('\n')

    return print_info
    
if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Problem Name > ')
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
