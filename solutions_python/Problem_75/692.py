def B(input):
    if input[0] == '0':
        del input[:1]
        f_comb = False
    else:
        f_comb = True
        comb = set([input[1][0], input[1][1]])
        comb_out = input[1][2]
        del input[:2]
     
    if input[0] == '0':
        del input[:1]
        f_oppose = False
    else:
        oppose = set([input[1][0], input[1][1]])
        f_oppose = True
        del input[:2]

    t_in=[c for c in input[1]]
    t_out = []
    for c in t_in:
        if t_out == []:
            t_out.append(c)
            continue
        
        if f_comb and comb == set([c, t_out[-1]]):
            t_out[-1] = comb_out
            continue
        if f_oppose and oppose.issubset(set(t_out).union([c])):
            t_out = []
            continue
        t_out.append(c)
    #if f_comb: print comb
    #if f_oppose: print oppose
    return t_out
if __name__ == '__main__':
    #str_in = 'B-test.in'
    str_in = 'B-small-attempt0.in'
    #str_in = 'B-large.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    for i, input in enumerate(open(str_in)):
        input = input.strip()
        if i == 0:
            T = [int(_s) for _s in input.split()[:1]]
            continue
        
        output = 'Case #' + str(i) + ': ' + str(B(input.split())).replace("'", "") + '\n'
        f_out.write(output)
        print output,

    f_out.close()
    
    print 'exit'

