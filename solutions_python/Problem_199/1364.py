import sys


def load_info(f):
    line = f.readline()
    out = int(line)
    return out    

def my_function(f, case_num):
    print_info = []
    line = f.readline().split(' ')
    pancakes, flipper = [x for x in line]
    pancakes = [x for x in pancakes]
    flipper = int(flipper)
    n = len(pancakes)
    i = 0
    res = 0
    while i + flipper <= n:
        if pancakes[i] == '-':
            for j in xrange(i,i+flipper):
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'
            res += 1
        i += 1

    if '-' in pancakes:
        res = 'IMPOSSIBLE'
    res = str(res)
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
