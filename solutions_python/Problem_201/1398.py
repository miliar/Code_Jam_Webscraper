import sys

    
def load_info(f):
    line = f.readline()
    out = int(line)
    return out    

def my_function(f, case_num):
    
    class counter(dict):
        def __missing__(self,key):
            return 0
    class my_list(list):
        stall_counter = counter()
        def insert_sort(self,x):
            i = -1
            while True:
                if self[i] == x:
                    break
                elif self[i] > x:
                    if i == -1:
                        self.append(x)
                    else:
                        self.insert(i+1,x)
                    break
                i -= 1
                
    print_info = []
    line = f.readline().split(' ')
    N, K = [int(x) for x in line]
    i = 0
    stalls = my_list()
    stalls.append(N)
    stalls.stall_counter[N] += 1
    while i < K-1:
        temp = stalls[0]/2
        stalls.stall_counter[stalls[0]] -= 1
        
        if stalls[0] == 1:
            pass
        elif stalls[0] == 2:
            stalls.insert_sort(1)
            stalls.stall_counter[1] += 1
        elif stalls[0]%2 == 1:
            stalls.insert_sort(temp)
            stalls.stall_counter[temp] += 2
        else:
            stalls.insert_sort(temp)
            stalls.stall_counter[temp] += 1
            stalls.insert_sort(temp-1)
            stalls.stall_counter[temp-1] += 1
            
        if not stalls.stall_counter[stalls[0]]:
            stalls.pop(0)
            
        i += 1
        
    if stalls[0] == 1:
        res = (0,0)
    elif stalls[0] == 2:
        res = (1,0)
    else:
        temp = stalls[0]/2
        if stalls[0]%2 == 1:
            res = (temp,temp)
        else:
            res = (temp,temp-1)
    print_info.append('Case #' + str(case_num+1) + ': %d %d' % (res))
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
