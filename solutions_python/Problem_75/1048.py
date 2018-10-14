import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename,'r')
    t = int(f.readline())
    
    for i in range(t):
        input_line = f.readline()
        inputs = input_line.split(' ')
        c = int(inputs[0])
        del(inputs[0])
        combines = {}
        for j in range(c):
            c_key = inputs[j][0:2]
            r_c_key = c_key[::-1]
            combines[c_key] = inputs[j][2]
            combines[r_c_key] = inputs[j][2]
        d = int(inputs[c])
        del(inputs[c])
        dels = {}
        for j in range(d):
            dels[inputs[j+c][0]] = inputs[j+c][1]
            dels[inputs[j+c][1]] = inputs[j+c][0]

        n = int(inputs[c+d])
        del(inputs[c+d])
        input_str = inputs[c+d]
        output = ['',]

        for j in range(n):
            clear_flag = False
            invoke = input_str[j]

            is_c = output[-1]+invoke
            if combines.has_key(is_c):
                output[-1] = combines[is_c]
                continue

            for item in output:
                if dels.has_key(item) and dels[item] == invoke:
                    output = ['',]
                    clear_flag = True
                    break;
            if clear_flag:
                continue
            
            output.append(invoke)
        
        print "Case #%d: [%s]"%(i+1,', '.join(output[1:]))
            
