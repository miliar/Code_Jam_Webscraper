'''
Created on Mar 20, 2012

@author: Wen
'''
def shift( s ):
    r = ''.join([ s[1:] , s[0] ] )
    if s == r:
        # same after shift
        return 'NULL'
    else:
        return r
    
def meat( A , B ):
    visited = {}
    count = 0
    for i in range(A+1,B):
        if i in visited :
            continue
        visited[i] = True
        cur = str(i)
        num = 1
        new =''
        for j in range(1,len(cur)) :
            new = shift( cur )
            if( new == 'NULL' ) :
                continue 
            if ( int(new) >= A and int(new) <= B ):
                num = num + 1
            cur = new
            visited[int(cur)] = True
        count = count + int( num*(num-1)/2 )
    return count
    
if __name__ == '__main__':
    fi = open ( './q3.in' , 'r' )
    fo = open ( './q3.out' , 'w' )
    size = int( fi.readline() ) 
    
    for j in range(0,size):
        x = [ int(x) for x in fi.readline().split() ]
        o = meat( x[0] , x[1] )
        fo.write( "Case #"+str(j+1)+': ') 
        fo.write( str(o) )
        fo.write( "\n" )            
    
    print("Done")
    
    
