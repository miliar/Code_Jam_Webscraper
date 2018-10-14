import sys

def _num_swaps(acts):
    acts.sort(key = lambda act:act[0])
    
    tot_swaps = 0
    gaps = []
    tot_par_time = [0, 0]
    either_time = 0
    prev = acts[-1][1] - 1440
    prev_par = acts[-1][2]
    for start, end, par in acts:
        tot_par_time[par] += end - start
        gap_time = start - prev
        if prev_par != par:
            tot_swaps += 1
            either_time += gap_time
        else:
            tot_par_time[par] += gap_time
            gaps.append((gap_time, par))
        prev = end
        prev_par = par
    
    gaps.sort(key = lambda gap: gap[0])    
    

    greedy_par = 0
    if tot_par_time[1] > tot_par_time[0]:
        greedy_par = 1

    other_par = (greedy_par + 1) % 2    
    
    #print(gaps)
    #print(either_time)
    while tot_par_time[other_par] + either_time < 720:
        #print(tot_par_time)
        gap_time, par = gaps.pop()
        if par == greedy_par:
            tot_swaps += 2
            tot_par_time[other_par] += gap_time
    
    return tot_swaps

def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        num_A, num_B = (int(val) for val in in_file.readline().strip().split())
        
        acts = []
        
        for _ in range(num_A):
            start, end = (int(val) for val in in_file.readline().strip().split())
            acts.append((start,end,0))
            
        for _ in range(num_B):
            start, end = (int(val) for val in in_file.readline().strip().split())
            acts.append((start,end,1))
        
        sol = _num_swaps(acts)
        
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
        
        
