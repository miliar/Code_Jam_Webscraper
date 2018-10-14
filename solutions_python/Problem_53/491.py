
input = open('A-large.in','r')
output = open('A-large.out','w')
out_strs = [];

n_lines = int(input.readline())
i = 1
for line in input.readlines():
    N = int(line.split()[0])
    K = int(line.split()[1])
    if ( K!=0 and (K+1)%(2**N) == 0 ):
        out_strs.append('Case #%d: ON\n'%i)
    else:
        out_strs.append('Case #%d: OFF\n'%i)
    i += 1
output.writelines(out_strs)
    
