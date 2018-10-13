'''
Created on 07.05.2011

@author: ikari
'''

def mystr(seq):
    str = '['
    str += ', '.join(seq)
    str += ']'
    return str

filename = "input.txt"
f = open(filename, "r")

T = int(f.readline())

for i in range(0, T):
    ss = f.readline().split()
    
    comb = []
    opp = []
    seq = []
    
    C = int(ss[0])
    
    for j in range(0, C):
        comb.append(ss[j+1])
        
    D = int(ss[C + 1])
    
    for j in range(0, D):
        opp.append(sorted(ss[C + 1 + j + 1]))
        
    for ch in ss[C + D + 3]:
        if len(seq) == 0:
            seq.append(ch)
        else:
            fin = False
            ''' Check for combine '''
            for c in comb:
                tmp = [seq[len(seq) - 1], ch]
                tmp.sort()
                if (c[0] == tmp[0] and c[1] == tmp[1]) or (c[1] == tmp[0] and c[0] == tmp[1]):
                    seq.pop()
                    seq.append(c[len(c) - 1])
                    fin = True
                    break
                
            if fin: continue
            
            for o in opp:
                if fin: break
                for s in seq:
                    tmp = [s, ch]
                    tmp.sort()
                    if o[0] == tmp[0] and o[1] == tmp[1]:
                        seq = []
                        fin = True
                        break
            
            if fin: continue
            
            seq.append(ch)

    print 'Case #' + str(i+1) + ': ' + mystr(seq)