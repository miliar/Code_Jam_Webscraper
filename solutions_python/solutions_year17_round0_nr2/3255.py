'''
Created on 8 apr 2017

@author: algestam
'''

def is_tidy(n):
    n_as_str = str(n)    
    sorted_n = "".join(sorted(n_as_str))
    return n_as_str == sorted_n

def solve(n):
    while not is_tidy(n):
        n_str = str(n)
        n_len = len(n_str)
        for i in range(n_len):
            if i < n_len -1:
                if int(n_str[i]) > int(n_str[1+i]):
                    to_remove = int(n_str[i+1:])
                    if to_remove == 0:
                        to_remove = 1
                    n = n - to_remove
                    break
    return n

for case in xrange(input()):
    N = int(raw_input())
    
    res = solve(N)

    print "Case #%i: %d" % (case+1, res)
    