#!/usr/bin/env python

# Lawnmower

def read_lawn(f):
    line = f.readline()
    words = line.split()
    N = int(words[0])
    M = int(words[1])
    
    lawn = []

    for i in range(0,N):
        row = []
        
        line = f.readline()
        words = line.split()
        
        for word in words:
            row.append( int(word) )
        
        lawn.append(row)
        
    return lawn

def print_lawn(lawn):
    for r in lawn:
        print r
    return

def check_patch(lawn,i,j):
    n = len(lawn)-1
    m = len(lawn[0])-1
    h = lawn[i][j]

    # check horizontal
    possible = (lawn[i][0] <= h and lawn[i][m] <= h)
    if possible:
         #print 'horizontal'
         for jj in range(0,m):
            possible &= lawn[i][jj] <= h    
            if not possible:    
                break   
    if possible:
        return possible
        
    # check vertical
    possible = (lawn[0][j] <= h and lawn[n][j] <= h)
    if possible:
         #print 'vertical'
         for ii in range(0,n):
            possible &= lawn[ii][j] <= h    
            if not possible:    
                break   
    if possible:
        return possible
        
    return possible


def spiralout_search(lawn):
    
    # dims
    N = len(lawn)
    M = len(lawn[0])        
    
    # center point
    cp = (N/2, M/2)

    # search (breadth first)
    sstack = []   
    sstack.append(cp)     
    explored = {}
    
    while len(sstack) != 0:
        p = sstack.pop()
        #print p
        
        if not check_patch(lawn,p[0],p[1]):
            return False
        
        # add to explored hash table
        explored[p] = None
        
        for i in range(-1,2):
            for j in range(-1,2):
                
                #print i,j
                new_p = (p[0]+i, p[1]+j)
                #print 'new_p', new_p
                
                if new_p in explored:
                    continue
                
                if new_p[0] >= N or new_p[0] < 0:
                    continue
                
                if new_p[1] >= M or new_p[1] < 0:
                    continue
                
                #print 'new_p', new_p
                sstack.append( new_p )    
    
    return True
    
    
def main():
    #f = open('B-input.txt', 'r')
    #f = open('B-small-attempt4.in', 'r')
    f = open('B-large.in', 'r')
    T = int(f.readline())

    out = open('output.txt', 'w')
    
    for i in range(T):   
        lawn = read_lawn(f)
        
        possible = spiralout_search(lawn)
    
        #print 'Case #', i
        #print possible
        #print_lawn(lawn)
        #raw_input()
        
        out.write('Case #'+str(i+1))
        if possible:
            out.write(': YES\n')  
        else:
            out.write(': NO\n')
        
if __name__ == '__main__': 
    main()
