'''
Created on 7 mai 2011

@author: nicolas
'''

import sys

def solve(n,l):
    #print l
    
    pos = {'O':1, 'B':1}
    time = 0
    lastpush = {'O':0, 'B':0}
    
    for bot,x in l:
        move = abs(x-pos[bot])
        if move > time - lastpush[bot]:
            time += move - (time - lastpush[bot])
        time += 1
        lastpush[bot] = time
        pos[bot] = x
        
    print 'Case #{}: {}'.format(n, time)
    #print ''


if __name__ == '__main__':
    filepath = sys.argv[1]
    file = open(filepath)
    
    file.readline()
    
    for t,line in enumerate(file.readlines()):
        l = line.split(None)
        n = int(l[0])
        seq = []
        for i in range(n):
            seq.append((l[2*i+1], int(l[2*i+2])))
        solve(t+1, seq)

