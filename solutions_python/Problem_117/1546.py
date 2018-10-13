t = int(input())

def init():
    global n , m , a
    l = str(input()).split(' ')
    n = int(l[ 0 ])
    m = int(l[ 1 ])
    a = []
    for i in range( 0 , n ):
        l = str(input()).split(' ')
        a.append( [ int( i ) for i in l ] )

def sol_small():
    one = 0
    cn = 0
    for t in a:
        one += t.count( 1 )
    #print( one )
    for t in a:
        if t.count( 2 ) == 0:
            one -= m
            cn += 1

    for i in range( 0 , m ):
        t = []
        for j in range( 0 , n ):
            t.append( a[ j ][ i ] )
        if t.count( 2 ) == 0:
            one = one - n + cn
    
    #print( one )
    
    if one == 0:
        return True
    else:
        return False

for i in range( 0 , t ):
    init()
    if sol_small() == True:
        print("Case" , "#{0}:".format( i + 1 ) , "YES")
    else:
        print("Case" , "#{0}:".format( i + 1 ) , "NO")
