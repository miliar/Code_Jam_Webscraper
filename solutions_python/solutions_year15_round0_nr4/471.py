# full symetry (vertical, horizontal) regarding the positioning of the nomino
# check for all the possibilities on one side only 

def countNominos(X):
    L = []
    for i in xrange((X+1)/2):
        L.append([i + 1, X - i, 2*i])
    return L


def has_complement(nomino, X, R, C):
    if nomino[1] == R and X > 3: # thus segregating the grid
        for j in xrange(X - nomino[1] + 1): #all perumtations
            complement = False
            for i in xrange(C/2 - nomino[1] + 1): #all left translations
                if (R*i + j) % X == 0:
                    complement = True
            if not complement :
                return False
    return True

if __name__ == '__main__':
    f = open('D-small-attempt2.in', 'r')
    o = open('D-small-attempt2.out', 'w')
    
    T = int(f.readline().strip())
    
    for i in range(1, T + 1):
        X, R, C = map(int, f.readline().strip().split())
        
        if (R*C % X) != 0:
            o.write('Case #' + str(i) + ': RICHARD\n')
            continue
        clear = False
        R, C = min(R, C), max(R, C)
        
        Nominos = countNominos(X)
        for nomino in Nominos:
            if nomino[0] > R or nomino[1] > C or (X == 4 and R == 2):
                o.write('Case #' + str(i) + ': RICHARD\n')
                clear = True
                break
        
        if not clear :
            o.write('Case #' + str(i) + ': GABRIEL\n')
    o.close()