from operator import mul

in_data = open('A-small-attempt0.in').readlines()
T=in_data[0]
in_data=in_data[1:]
outfile = open('result', 'w')
case_no = 0

while len(in_data)>0:
    case_no += 1
    tmp = in_data[0]
    a, b = [int(x) for x in tmp.strip().split()]
    p = in_data[1]
    p = [float(x) for x in p.strip().split()]
    in_data = in_data[2:]
    res = 100000000
    # go back
    for gb in range(a+1):
        if (gb==a):
            p_corr = 0
        else:
            p_corr = reduce(mul, p[:(a-gb)])
        
        p_wrong = 1-p_corr
        
        k_corr = gb*2 + (b-a) + 1
        k_wrong = k_corr + b + 1
        
        ave = p_corr*k_corr + p_wrong * k_wrong
        if ave < res:
            res = ave
    
    # return
    if res > b + 2:
        res = b + 2
        
    out = 'Case #' + str(case_no) + ': ' + str(res) + '\n'
    outfile.write(out)
    
    
outfile.close()



# END