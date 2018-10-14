# -*- coding: utf-8 -*-
# @Author: Pandarison
# @Date:   2017-04-15
# @Last Modified time: 2017-04-15

from z3 import *


data = [
    ['A', '?', '?', '?'],
    ['?', 'A', 'B', '?'],
    ['?', '?', '?', '?']
]

data = []

T = int(raw_input())
for test_case in range(1, T+1):
    R,C = raw_input().split()
    data = []
    for i in range(int(R)):
        data.append(list(raw_input()))
    solver = Solver()

    domain = set(reduce(lambda x,y: x+y,data))
    if '?' in domain:
        domain.remove('?')

    dictionary = {}
    d_id = 1

    for x in domain:
        dictionary[x] = d_id
        dictionary[d_id] = x
        d_id += 1

    #print(dictionary[1])

    DATA = [ [ Int("%s_%s" % (i+1, j+1)) for j in range(len(data[0])) ]
          for i in range(len(data)) ]

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '?':
                solver.add(DATA[i][j] == dictionary[data[i][j]])

    for i in range(len(data)):
        for j in range(len(data[0])):
            solver.add(0 < DATA[i][j])
            solver.add(DATA[i][j] < d_id)

    for i in range(len(data)):
        for j in range(len(data[0])):
            for p in range(len(data)):
                for q in range(len(data[0])):
                    for a in range(len(data)):
                        for b in range(len(data[0])):
                            if i<=a<=p or p<=a<=i:
                                if j<=b<=q or q<=b<=j:
                                    solver.add(Implies(DATA[i][j] == DATA[p][q], DATA[a][b] == DATA[i][j]))
                    
    if solver.check() == sat:
        m = solver.model()
        r = [ [ m.evaluate(DATA[i][j]) for j in range(len(data[0])) ] 
              for i in range(len(data)) ]
        r = list(r)
        for i in range(len(r)):
            r[i] = map(lambda x: dictionary[int(str(x))], r[i])
        print("Case #%d:"%test_case)
        for x in r:
            print(''.join(x))
