#!/usr/bin/env python

#infile = "B-large.in"
infile = "B-small-attempt0.in"
#infile = "B-sample.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    lst = [value for value in fsrc.readline().split()]
    C = int(lst.pop(0))
    combines = lst[:C]
    lst = lst[C:]
    D = int(lst.pop(0))
    oposites = lst[:D]
    game = lst[-1]

    #print 'C:', C, 'combines:', combines, 'D:', D, 'oposites:', oposites, 'game:', game
    c_dict = {}
    for c in combines:
        c_dict[c[:2]] = c[2]
        c_dict[c[1] + c[0]] = c[2]
    
    d_dict = {}
    for d in oposites:
        d_dict[d[0]] = d[1]
        d_dict[d[1]] = d[0]

    res_lst = [' ']

    for card in game:
        #print 'List:', res_lst
        #print 'Card:', card
        # check combines
        last_card = res_lst[-1]
        if c_dict.has_key(last_card + card):
            res_lst[-1:] = c_dict[last_card + card]
            continue
        # check oposites
        if d_dict.has_key(card) and d_dict[card] in res_lst:
            res_lst = [' ']
            continue
        # add to list
        res_lst.append(card)

    res = "Case #%s: " %(t+1, ) 
    
    res += '[' + ', '.join(res_lst[1:]) + ']\n'
    print res,
    fres.write(res)

fsrc.close()
fres.close()
