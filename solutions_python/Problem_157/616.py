from codejam import *

def read_file(f):
    case = []
    case.append(read_int_list(f))
    case.append(read_string(f))
    #print(case)
    return case

def solver(case):
    lst, string = case
    test_i, test_j, test_k = False, False, False
    d = {'1' : ('1', 1), 'i' : ('i', 1), 'j' : ('j', 1), 'k' : ('k', 1),
         '11' : ('1', 1), '1i' : ('i', 1), '1j' : ('j', 1), '1k' : ('k', 1),
         'i1' : ('i', 1), 'ii' : ('1', -1), 'ij' : ('k', 1), 'ik' : ('j', -1),
         'j1' : ('j', 1), 'ji' : ('k', -1), 'jj' : ('1', -1), 'jk' : ('i', 1),
         'k1' : ('k', 1), 'ki' : ('j', 1), 'kj' : ('i', -1), 'kk' : ('1', -1)}
    
    def mult(a, b):
        key = a[0] + b[0]
        if key in d:
            val = d[key]
        return (val[0], val[1] * a[1] * b[1])

    current = ('1', 1)
    for repeat in range(lst[1]):
        for letter in string:
            current = mult(current, (letter, 1))
            if (not test_i) and current == ('i', 1):
                test_i = True
                current = ('1', 1)
            if test_i and (not test_j) and current == ('j', 1):
                test_j = True
                current = ('1', 1)
    if test_i and test_j and (not test_k) and current == ('k', 1):
        test_k = True
        
    #print(test_i, test_j, test_k)
    if test_i and test_j and test_k:
        #print('YES')
        return 'YES'
    #print('NO')
    return 'NO'

solve('C-small-attempt0', read_file, solver)
