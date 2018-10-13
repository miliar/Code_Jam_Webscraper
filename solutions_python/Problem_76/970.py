from pprint import pprint
import operator
from itertools import combinations

def p2d(tab):
    for e in tab:
        print(e)

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    cache = {}
    
    for test in range(N):
        total = 0
        n = int(fin.readline().replace("\n", ""))
        l = fin.readline().replace("\n", "")
        c = [int(g) for g in l.split(" ")]
        
        print n
        pprint(c)
        
        found = False
        max = 0
        
        xa = reduce(lambda x, y: x^y, c)
        
        if xa == 0:       
            for r in xrange(1, n):
                for i in combinations(c, r): 
                    xor = reduce(lambda x, y: x^y, i)                    
                                      
                    if(xa == xor ^ xor):
                        found = True
                        sm = sum(i)
                        max = sm if sm > max else max
              
        print found, max
                
        total = 'NO' if not found else max
                
        sol = "Case #" + str(test+1) + ": " + str(total) + "\n"
        print(sol)
        fout.write(sol)
