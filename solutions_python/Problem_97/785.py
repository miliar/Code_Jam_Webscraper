#!/usr/bin/env python

from codejam import CodeJam

def process_case(line):
   
    recycled = set() 
    A_s, B_s = line.split(' ')
    A = int(A_s)
    B = int(B_s)

    length = len(str(A))
    range_len = range(1, length)

    for n in range(A, B):
        n_l = list(str(n))
        for i in range_len:
            if n_l[-i] > B_s[0] or \
                        n_l[-i] < A_s[0] or n_l[-i] == '0':
                continue
            #m_l = n_l[-i:] + n_l[:-i] 
            #m_s = ''.join(m_l)
            #m = int(m_s)
            m = int(''.join(n_l[-i:] + n_l[:-i])) 
            if A <= n < m <= B:
                recycled.add((n, m))
    return len(recycled)

if __name__ == '__main__':
    codejam = CodeJam()
    codejam(process_case)
