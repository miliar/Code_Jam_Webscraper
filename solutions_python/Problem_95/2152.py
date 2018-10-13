import itertools as it
import string
from sys import stdin
frm = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz'
to =  'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq'
table = string.maketrans(frm, to)    

def solve(G):
    return G.translate(table)
    
def main():
    n = int(next(stdin))
    for i, line in enumerate(stdin):
        G = line.strip()
        print 'Case #%d: %s' % (i+1, solve(G))
    
if __name__ == '__main__':
    main()
