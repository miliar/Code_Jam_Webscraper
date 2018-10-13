import sys

if __name__ == "__main__":
    fin = open( 's.in', 'r', encoding = 'utf8' )
    fout = open( 's.out', 'w', encoding = 'utf8' )
    
    N = int(fin.readline().strip())
    
    for _n in range(N):
        r, c = map(int, fin.readline().strip().split())     
        
        t = []
        for i in range(r):
            t.append(list(fin.readline().strip()))
            
        err = 0
        for i in range(r-1):
            for j in range(c-1):
                if t[i].count('#')%2!=0:
                    err = True
                    break                
                if (t[i][j], t[i][j+1], t[i+1][j], t[i+1][j+1])==('#','#','#','#'):
                    t[i][j], t[i][j+1], t[i+1][j], t[i+1][j+1] = '/', '\\', '\\', '/'
        
        for _t in t:
            if '#' in _t:
                err = True
        
        fout.write('Case #{}:\n'.format(_n+1))
        
        if err:
            fout.write('Impossible\n')
        else:
            for _t in t:
                fout.write(''.join(_t))
                fout.write('\n')