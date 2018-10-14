import random

filename = 'c:/users/Nick/Documents/Google Code Jam 2017/B-large.in'
input = [l.rstrip() for l in open(filename)]
N = int(input[0])

def is_tidy(N):
    for idx in range(0, len(N)-1):
        if(N[idx] > N[idx+1]):
            return False
    return True
    

def solve(N):
    '''Return the largest tidy integer <= N (N is a decimal string)'''
    Nl = list(N)
    # convert digits to integers
    Nl = [int(d) for d in Nl]
    idx = 0
    already_tidy = True
    for idx  in range(len(Nl)-1):
        if(Nl[idx] > Nl[idx+1]):
            already_tidy = False
            Nl[idx] -= 1
            for idx2 in range(idx+1, len(Nl)):
                Nl[idx2] = 9
                idx = idx2
    if(already_tidy):
        return N
    # convert back to characters
    Nl = ['%d' % d for d in Nl]
    new_N = int(''.join(Nl))
    return solve('%d' % new_N)
    
def brute_force(N):
    Ni = int(N)
    while(is_tidy('%d' % Ni) == False):
        Ni -= 1
    return '%d' % Ni
    
def test_solve():
    for i in range(1000000):
        N = random.randint(1, 10000)
        soln_brute = brute_force('%d' % N)
        soln = solve('%d' % N)
        if(soln != soln_brute):
            print('Error: %d, %d (brute)' % (soln, soln_brute))

out_fd = open(filename.replace('.in', '.out'), 'w')
for t_i in range(1, N+1):
    soln = solve(input[t_i])
    print('Case #%d: %s' % (t_i, soln))
    out_fd.write('Case #%d: %s\n' % (t_i, soln))
out_fd.close()