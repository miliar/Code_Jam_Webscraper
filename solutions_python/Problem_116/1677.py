'''
Created on Apr 13, 2013

@author: santosh
'''

if __name__ == '__main__':
    T = int(input())
    for t in xrange(T):
        ar = list()
        for i in xrange(4): ar.append(raw_input())
        pieces = list()
        pieces.extend(ar)  # rows
        pieces.extend([''.join([ar[j][i] for j in xrange(4)]) for i in xrange(4)])  # cols
        pieces.extend([''.join([ar[i][i] for i in xrange(4)]) , ''.join([ar[i][3 - i] for i in xrange(4)])])# diagonals
        p='.'
        for col in pieces:
            if col.replace('T', 'X') == 'XXXX': 
                p='X'
                break
            elif col.replace('T', 'O') == 'OOOO': 
                p='O'
                break
        if p != '.' :  print 'Case #%d: %s won' % (t + 1, p)     
        else :
            if '.' in ''.join(pieces): print 'Case #%d: %s'%(t+1,'Game has not completed')
            else : print 'Case #%d: %s'%(t+1,'Draw')
            
        raw_input()  # consumes black line
