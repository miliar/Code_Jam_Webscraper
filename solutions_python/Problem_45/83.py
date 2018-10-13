'''
Created on 2009. 9. 13.

@author: natas999@gmail.com
'''

def process(cells, rels):
    depth = len(rels)
    seqs = [[rels[i // (depth**d) % depth] for d in range(depth)] for i in range(depth**depth)]
    nox = list()
    for x, seq in enumerate(seqs):
        for i in seq:
            if seq.count(i) != 1 and not x in nox:
                nox.append(x)
    rel_x = list()
    for i, x in enumerate(seqs):
        if not i in nox:
            rel_x.append(x)
#    print rel_x
#    return
    sums = list()
    for i in rel_x:
        sums.append(subprocess([range(1, int(cells)+1)], i))
    return min(sums)

def subprocess(cells, rels):
    sum = 0
#    print rels
#    print rels, cells
    for i in rels:
#        print i
        sc = getSubCell(cells, i)
#        print cells, sc
        ix = cells[sc].index(i)
        left = cells[sc][:ix]
        cells.append(left)
        right = cells[sc][ix+1:]
        cells.append(right)
        cells.pop(sc)
#        print left, right
        sum += len(left) + len(right)
    return sum

def getSubCell(cells, rel):
    for i, subcell in enumerate(cells):
        if rel in subcell:
            return i

def main(input_fn):
    try:
        f = open(input_fn, 'r')
        o = open(input_fn+'.out', 'w')
    except IOError:
        print "Input file %s dos not exists" % (input_fn, )
        return 2
    
    lines = int(f.readline())
    
    for i in range(lines):
        cells, rels = f.readline().split()
#        print rows, columns
        release = f.readline().split()
        release = [int(k) for k in release]
        ret = process(cells, release)
        print ret
#        print matrix
        o.write('Case #' + str(i+1) + ': ' + str(ret) + '\n')
    
import sys
if __name__ == '__main__':
    main(sys.argv[1])