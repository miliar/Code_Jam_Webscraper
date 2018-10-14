import random
from math import ceil, floor

filename = 'c:/users/Nick/Documents/Google Code Jam 2017/C-small-2-attempt0.in'
input = [l.rstrip() for l in open(filename)]
N = int(input[0])

def sub_largest_2(K):
    largest_power_of_2 = 1
    while(K >= (largest_power_of_2 << 1)):
        largest_power_of_2 <<= 1
    return K - (largest_power_of_2 >> 1)
    
def get_largest_2(K):
    largest_power_of_2 = 1
    while(K >= (largest_power_of_2 << 1)):
        largest_power_of_2 <<= 1
    return largest_power_of_2
    

def empty_stalls(N, K):
    if(N <= 1):
        return (0,0)
    left = ceil(N/2)-1
    right = floor(N/2)
    if(K == 1):
        return (right, left)
    else:
        if(K % 2 == 0):
            return empty_stalls(right, (K >> 1))
        else:
            return empty_stalls(left, (K >> 1))
            
def solve(s):
    N, K = s.split()
    N = int(N)
    K = int(K)
    a,b = empty_stalls(N, K)
    return '%d %d' % (a,b)
        
def get_ls_rs(stalls, position):
    ls = 0
    rs = 0
    stop_counting_ls = False
    stop_counting_rs = False
    for i in range(1, len(stalls)):
        if(position - i >= 0 and stop_counting_ls == False):
            if(stalls[position - i] == 'O'):
                stop_counting_ls = True
            else:
                ls += 1
        if(position + i < len(stalls) and stop_counting_rs == False):
            if(stalls[position + i] == 'O'):
                stop_counting_rs = True
            else:
                rs += 1
    return (ls, rs)
    
def brute_force(N, K):
    stalls = ['.']*N
    while(K >= 1):
        parameters_by_stall = []  # store -min(L_s, R_s), -max(L_s, R_s), stall_position
        for i in range(N):
            if(stalls[i] == '.'):
                L_s, R_s = get_ls_rs(stalls, i)
                parameters_by_stall.append([-min(L_s, R_s), -max(L_s, R_s), i])
        parameters_by_stall.sort()
        neg_min, neg_max, chosen_stall = parameters_by_stall[0]
        stalls[chosen_stall] = 'O'
        if(K == 1):
            return (-neg_max, -neg_min)
        K -= 1
        
def test():
    for i in range(100):
        N = random.randint(1,100)
        K = random.randint(1,N)
        if(empty_stalls(N,K) != brute_force(N,K)):
            print('Fail: N=%d, K=%d' % (N, K))
            return False
    print('Test passed')
    return True


out_fd = open(filename.replace('.in', '.out'), 'w')
for t_i in range(1, N+1):
    soln = solve(input[t_i])
    out_string = 'Case #%d: %s\n' % (t_i, soln)
    print(out_string, end='')
    out_fd.write(out_string)
out_fd.close()