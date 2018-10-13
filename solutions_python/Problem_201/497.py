import sys


def last_limits(gap, num_people):
    stalls = [[gap,1]]
    tot = 0
    while tot < num_people:
        cand, num = stalls.pop(0)
        tot += num
        to_half = cand - 1
        if to_half % 2 == 0:
            small, big = to_half//2, to_half//2
        else:
            small, big = to_half//2, to_half//2 + 1
        for val in (big, small):
            if len(stalls) > 0 and stalls[-1][0] == val:
                stalls[-1][1] += num
            else:
                stalls.append([val, num])
    return big, small

def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        gap, num_people = (int(val) for val in in_file.readline().strip().split())
        #Call func for solution
        big, small = last_limits(gap, num_people)
        out_file.write("Case #{}: {} {}\n".format(case, big, small))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'C-sample'
        #name = 'C-small-1-attempt0'
        #name = 'C-small-2-attempt0'
        name = 'C-large'
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
        
        
