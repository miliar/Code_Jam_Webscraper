# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:32:19 2012

@author: mmunnik
"""

f = open("C-large.in", 'r')
g = open("C_large_answer.txt", 'w')

N = int(f.readline())
 
for i,line in enumerate(f):
    g.write("Case #%d: " % (i+1))
    count = 0
    
    # A and B
    A, B = line.split()
    A = int(A)
    B = int(B)

    for i in range(A, B+1):
        if i >= 12:
            n = str(i)
            n2 = 2*n
            L = len(n)
            m_list = []
            
            for j in range(1, L):
                m = n2[j:(j+L)]
                m = int(m)

                if (m <= B) and (m > i) and (m not in m_list):
                    count += 1
                    m_list.append(m)
    
    g.write("%d\n" % count)
f.close()
g.close()