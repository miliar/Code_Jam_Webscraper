filename = 'c:/users/Nick/Documents/Google Code Jam 2017/A-large.in'
input = [l.rstrip() for l in open(filename)]
N = int(input[0])


def solve(S, K):
    current_pos = 0
    flips = 0
    Sl = list(S)
    # while current_pos + K - 1 < len(S):
    # find the first -
    # flip that plus the next K-1 pancakes
    while(True):
        if('-' not in Sl):
            break
        current_pos = Sl.index('-')
        if(current_pos < 0):
            break
        if(current_pos + K > len(Sl)):
            break
        for k_i in range(current_pos, current_pos+K):
            if(Sl[k_i] == '+'):
                Sl[k_i] = '-'
            else:
                Sl[k_i] = '+'
        flips += 1
    # when the while loop ends, if there are any - pancakes, we failed
    # otherwise return the number of flips
    if('-' in Sl):
        return None
    else:
        return flips
    
out_fd = open(filename.replace('.in', '.out'), 'w')
for t_i in range(1, N+1):
    S, K = input[t_i].split()
    soln = solve(S, int(K))
    if(soln == None):
        print('Case #%d: IMPOSSIBLE' % t_i)
        out_fd.write('Case #%d: IMPOSSIBLE\n' % t_i)
    else:
        print('Case #%d: %d' % (t_i, soln))
        out_fd.write('Case #%d: %d\n' % (t_i, soln))
out_fd.close()