l = []

import numpy

with open('/home/vivanov/Downloads/A-large.in') as f:
    lines = f.read().splitlines()[1:]
    b = []
    l = []
    for k in range(len(lines)):
        line = lines[k]
        if line == '' or k == len(lines) - 1 : 
            l.append(numpy.array(b))
            b = []
        else:
            b.append([i for i in line])
            
    l = numpy.array(l)


def check(l):
    if 'X' not in l and '.' not in l:
        return 'O'
    elif 'O' not in l and '.' not in l:
        return 'X'

#print check(['X','T','X','X'])

import itertools

def won(a):
    l = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            l.append(set(a[:][:,j]))
            l.append(a[i])
    diag1 = [a[i][i] for i in range(len(a))]
    diag2 = [a[i][len(a[0]) -1 - i] for i in range(len(a))]
    l.append(diag1)
    l.append(diag2)
    return sorted(set([check(i) for i in l]))[-1], '.' not in itertools.chain(*a)
    
def decide((a,b)):
    if not a and b == True:
        return 'Draw'
    elif not a and b == False:
        return 'Game has not completed'
    elif a :
        return a + ' won'

#print decide(won(l[4]))     

with open('tic_tac_sample_a0.out', 'w') as f :
    to_write = []
    for i in range(len(l)):
        to_write.append(('Case #%s: ' %(i+1)) + decide(won(l[i])) + '\n')
    f.writelines(to_write)
