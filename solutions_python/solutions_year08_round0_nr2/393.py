import copy

def list_cmp1 ( a , b ) :
    if a [ 0 ] < b [ 0 ] :
        return -1 
    return 1 

def list_cmp2 ( a , b ) :
    if a [ 1 ] < b [ 1 ] :
        return -1
    return 1
    

def conv2min ( time ) :
    t0 = time [ 0 ].split ( ':' )
    t1 = time [ 1 ].split ( ':' )
    return [ int ( t0 [ 0 ] ) *60 + int ( t0 [ 1 ] ) , int ( t1 [ 0 ] ) *60 + int ( t1 [ 1 ] ) ]


file_contents = open ( 'ttinput_large.txt' )

file_write = open ( 'output.txt' , 'w+' )

test_case = int ( file_contents.readline ( ) )

cnt = 0
cnt1 = 0

while cnt < test_case :

    tat = int ( file_contents.readline ( ) )

    n  =  file_contents.readline ( ).split ( )

    na = int ( n [ 0 ] )
    nb = int ( n [ 1 ] )

    na_lt = [ ]
    nb_lt = [ ]

    cnt1 = 0
    while cnt1 < na :
        time = file_contents.readline ( ).split ( )
        time = conv2min ( time )
        na_lt.append ( time )
        cnt1 += 1

    cnt1 = 0
    while cnt1 < nb :
        time = file_contents.readline ( ).split ( )
        time = conv2min ( time )
        nb_lt.append ( time )
        cnt1 += 1

    na_lt_dup = copy.deepcopy ( na_lt )
    nb_lt_dup = copy.deepcopy ( nb_lt )


    na_lt.sort ( list_cmp1 ) #arr time
    nb_lt.sort ( list_cmp1 )

    na_lt_dup.sort ( list_cmp2 ) #dest time
    nb_lt_dup.sort ( list_cmp2 )



    for x in na_lt_dup :
        for y in nb_lt :
            if int ( x [ 1 ] ) + tat <= y [ 0 ] :
                nb -= 1
                nb_lt.remove ( y )
                break


    for x in nb_lt_dup :
        for y in na_lt :
            if int ( x [ 1 ] ) + tat <= y [ 0 ] :        
                na -= 1
                na_lt.remove ( y ) 
                break

    file_write.write ( "Case #%d: %d %d\n" %( cnt + 1 , na , nb ) )                
    
    cnt += 1

