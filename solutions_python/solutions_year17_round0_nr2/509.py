import sys

def last_rise(limit):
    ret = 0
    prev = limit[0]
    for index in range(1, len(limit)):
        cand = limit[index]
        if prev != cand:
            if cand > prev:
                prev = cand
                ret = index
            else:
                return ret
    return None
            

def tidy_num(limit):
    i = last_rise(limit)
    if i is None:
        return limit
    else:
        cand = limit[:i] + str(int(limit[i]) - 1) + '9'*len(limit[i+ 1:])
        return str(int(cand))
    
def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        limit = in_file.readline().strip()
        #Call func for solution
        sol = tidy_num(limit)
        out_file.write("Case #{}: {}\n".format(case, sol))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'B-sample'
        #name = 'B-small-attempt0'
        name = 'B-large'
        file_input = open(path + name + '.in', 'r')
        out_full_name = path + name +'.out'
        if alt_out:
            out_full_name = path + name + "naive" +'.out'            
        file_output = open(out_full_name,'w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        
        
