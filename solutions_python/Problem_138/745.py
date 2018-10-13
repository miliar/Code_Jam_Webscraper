OUT_STR = 'Case #%d: %d %d'
def read_case(number, in_fl, out_fl):
    seq_len = int(in_fl.readline().strip())
    Naomi =  map(float, in_fl.readline().strip().split())
    Ken =  map(float, in_fl.readline().strip().split())
    Naomi.sort()
    Ken.sort()
    count_war = 0
    count_dwar = 0
    k_top = n_top = seq_len-1
    for k in range(seq_len-1, -1, -1):
        if Naomi[k]>Ken[k_top]:
            count_war +=1
        else: k_top -= 1
        if Naomi[n_top]>Ken[k]:
            n_top -=1
            count_dwar +=1
    out_fl.write(OUT_STR %(number, count_dwar, count_war))
    
input_fl = open('D-large.in','r')
output_fl = open('D-large.out', 'w')
cases = int(input_fl.readline().strip())
for n in range(1, cases+1):
    read_case(n, input_fl, output_fl)
    if n!=cases: output_fl.write('\n')
input_fl.close()
output_fl.close()
