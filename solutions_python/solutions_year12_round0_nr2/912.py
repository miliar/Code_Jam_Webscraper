'''
Created on Mar 20, 2012

@author: Wen
'''
def meat( i ):
    iA = i.split()
    ng = int(iA[0])
    ns = int(iA[1])
    np = int(iA[2])
    count = 0 
    for j in range( 0 , ng ):
        total = int(iA[3+j])
        low = total // 3
        res = total % 3
        if low >= np :
            count = count + 1
            continue
        if res == 0:
            if (low + 1 >= np) and (low - 1 >= 0 ) and ( ns > 0 ):
                count = count + 1
                ns = ns - 1
        if res == 1:
            if low +1 >= np :
                count = count + 1
        if res == 2:
            if low + 1 >= np :
                count = count + 1
            elif ( low + 2 >= np ) and ( ns > 0 ):
                count = count + 1
                ns = ns - 1
    return count
    
if __name__ == '__main__':
    fi = open ( './q2l.in' , 'r' )
    fo = open ( './q2l.out' , 'w' )
    size = int( fi.readline() ) 
    
    for j in range(0,size):
        i = fi.readline()
        o = meat( i )
        fo.write( "Case #"+str(j+1)+': ') 
        fo.write( str(o) ) 
        fo.write( "\n" )                
    
    print("Done")
    
    
