from sys import stdin
from unittest import result

def main():
    n_cases = int(stdin.readline()) 

    for i_case in range(1, n_cases+1):
        tictac = [ [ 0 for i in range(4) ] for j in range(4) ]
        for j1 in range(4):
            seq = stdin.readline()
            for j2 in range(4):
                tictac[j1][j2] = str(seq[j2])
                
        resultsX  = [['X','X','X','X'],['T','X','X','X'],['X','T','X','X'],['X','X','T','X'],['X','X','X','T']]
        resultsO  = [['O','O','O','O'],['T','O','O','O'],['O','T','O','O'],['O','O','T','O'],['O','O','O','T']]
        
        fin = False
        draw = True 
        # orisontales
        for j1 in range(4):
            if tictac[j1] in resultsX:
                fin = True
                result = 'X' 
                break
            elif tictac[j1] in resultsO:
                fin = True
                result = 'O' 
                break
            
        # verticales
        if not fin:
            for j1 in range(4):
                ver = [tictac[i+4%4][j1] for i in range(4)]
                if ver in resultsX:
                    fin = True
                    result = 'X' 
                    break
                elif ver in resultsO:
                    fin = True
                    result = 'O' 
                    break
            
        # crusados
        if not fin:
            orisontal = [[tictac[i][i] for i in range(4)],[tictac[i][3-i] for i in range(4)]]
            for ori in orisontal:
                if ori in resultsX:
                    fin = True
                    result = 'X' 
                    break
                elif ori in resultsO:
                    fin = True
                    result = 'O' 
                    break
        # ver enpate
        if not fin:
            for j1 in range(4):
                if draw:
                    for j2 in range(4):
                        draw = draw and not tictac[j1][j2] == '.'
                else:
                    break
        
        
        if fin:
            print 'Case #'+str(i_case)+': '+result+' won'
        elif draw:
            print 'Case #'+str(i_case)+': Draw'
        else:
            print 'Case #'+str(i_case)+': Game has not completed'
        seq = stdin.readline()


if __name__ == '__main__':
    main()