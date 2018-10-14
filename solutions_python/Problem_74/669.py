def A(input):
    N = int(input[0])
    time_col = {'O':0, 'B':0}
    pos_col = {'O':1, 'B':1}
    time = 0

    for n in range(N):
        col = input[n*2+1]
        antcol = 'B' if col == 'O' else 'O'
        pos = int(input[n*2+2])
        time_col[col] += abs(pos-pos_col[col])+1
        if time_col[antcol] >= time_col[col]:        
            time_col[col] = time_col[antcol]+1
        pos_col[col] = pos
                          
    return max(time_col.values()) 

if __name__ == '__main__':
    #str_in = 'A-small-attempt0.in'
    str_in = 'A-large.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    for i, input in enumerate(open(str_in)):
        input = input.strip()
        if i == 0:
            A_T = [int(_s) for _s in input.split()[:1]]
            continue
        
        output = 'Case #' + str(i) + ': ' + str(A(input.split())) + '\n'
        f_out.write(output)
        print output,

    f_out.close()
    
    print 'exit'
    #print A_D, set_A

