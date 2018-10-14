set_A = set([])
A_L, A_D = 0, 0
def A(input):
    s = ''
    isUnique = True
    seq = []
    for c in input:
        if c == '(':
            isUnique = False
            continue
        if not isUnique:
            if c == ')':
                seq.append(set(list(s)))
                s = ''
                isUnique = True
                continue
            else:
                s += c
                continue

        seq.append(set(c))

    ans_num = 0
    for s in set_A:
        for i, c in enumerate(seq):
            if s[i] not in c:
                break
        else:
            ans_num += 1
    return str(ans_num)

    """
    l_set = [set([])] * A_L
    for s in set_A:
        for i, c in enumerate(s):
            l_set[i].add(c)
    
    ans = ['']
    for i, c_tuple in enumerate(seq):
        c_tuple = [_c for _c in c_tuple if _c in l_set[i]]
        print i, len(c_tuple)
        #ans = [_str + _c for _str in ans for _c in c_tuple]
    ans = [_str for _str in ans if _str in set_A]
    
    return len(ans)
    """

if __name__ == '__main__':
    #str_in = 'A-small-attempt1.in'
    str_in = 'A-large.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    for i, input in enumerate(open(str_in)):
        input = input.strip()
        if i == 0:
            A_L, A_D = [int(_s) for _s in input.split()[:2]]
            continue
        if i <= A_D:
            set_A.add(input)
            continue

        f_out.write('Case #' + str(i - A_D) + ': ' + A(input) + '\n')
        #f_out.write('Case #' + str(i) + ': \n' + B(input))
        #f_out.write('Case #' + str(i) + ': ' + C(input) + '\n')

    f_out.close()
    #print A_D, set_A

