from itertools import product, combinations, combinations_with_replacement
from operator import mul

def perms(it):
    ret = []
    for i in range(len(it)):
        ret.append(it[i:]+it[:i])
    return ret

def result(text):
    A, B = [i for i in text.split()]
    d = len(str(A))
    result = 0
    checked = {}
    for comb in product(*(['0123456789']*d)):
    #for comb in combinations_with_replacement('0123456789', d):
        perm = set(perms(comb))
        pm = min(perm)
        if pm in checked:
            continue
        #perm.sort()
        num = 0
        for i in perm:
            p = ''.join(i)
            if A <= p <= B and i[0]!='0':
                #print p
                num +=1
        checked[pm] = None
        result += num*(num-1)/2

    return result

def solve(filename):
    fi = open(filename)
    fo = open(filename+'.out', 'w')
    N = int(fi.readline().strip())
    for i,line in enumerate(fi):
        line = line.rstrip('\n')
        wr = 'Case #%d: %s'%(i+1, result(line))
        print line
        print wr
        if i != N-1:
            wr += '\n'
        fo.write(wr)
    fo.close()
    fi.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv)>1:
        solve(sys.argv[1])
    else:
        solve('sample.in')
