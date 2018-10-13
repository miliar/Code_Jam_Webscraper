#!/usr/bin/env python
""" All your base """
import sys

def analyse_test_case(text):
    chars = []
    values = []
    tV = []
    for t in text :
        if t in chars :
            tV.append(values[chars.index(t)])
        elif len(chars) == 0:
            chars = [t]
            values = [1]
        elif len(chars) == 1 :
            chars.append(t)
            values.append(0)
        else :
            chars.append(t)
            values.append(len(values))
    if len(chars) == 1 : #uniary case 
        chars.append(' ')
        values.append(0)

    #print(text)
    print('chars,values',chars,values)
    base = len(chars)
    # answer will never exceed 10*18
    base10_Ans = [0 for i in range(19)]
    no = 0
    for t,i in zip(text,range(len(text))) :
        b_ind = len(text) - i
        #print(t,i, base**i, b_ind)
        bV = values[chars.index(t)]
        if bV <> 0 :
            no = no + base **(b_ind-1) *  bV

    return no
            
    

def analyse_datafile(datafile):
    f = file(datafile)
    lines = f.readlines()
    f.close()
    N = int(lines[0].strip())
    print('file "%s" contains %i cases' % (datafile,N))
    count = 1
    output = []
    for case_raw in lines[1:N+1]:
        case = case_raw.strip()
        print(case)
        no=analyse_test_case(case)
        output.append("Case #%i: %i" % (count,no))
        print(output[-1])
        count = count + 1
                      
    return output


output =  analyse_datafile(sys.argv[1])

fout = file(sys.argv[1]+'_output','w')
fout.write('\n'.join(output))
fout.close()
