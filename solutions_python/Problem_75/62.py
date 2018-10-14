T = input()
for t in range(T):
    toks = raw_input().split()
    C = int(toks[0])
    combine = toks[1:1+C]
    combine_dict = {}
    for elt in combine:
        combine_dict[elt[0]+elt[1]] = elt[2]
        combine_dict[elt[1]+elt[0]] = elt[2]
    toks = toks[1+C:]
    D = int(toks[0])
    opposed = toks[1:1+D]
    toks = toks[1+D:]
    N = int(toks[0])
    s = toks[1]
    element_list = []
    for ch in s:
        if len(element_list)>0 and (element_list[-1] + ch) in combine_dict:
            key = element_list[-1] + ch
            element_list = element_list[:-1]
            element_list.append(combine_dict[key])
        else:
            clear = False
            for o in opposed:
                if o[0]==ch and o[1] in element_list:
                    clear = True
                    break
                if o[1]==ch and o[0] in element_list:
                    clear = True
                    break
            if clear:
                element_list = []
            else:
                element_list.append(ch)        
    print 'Case #%d: %s' % (t+1, str(element_list).replace("'", ''))