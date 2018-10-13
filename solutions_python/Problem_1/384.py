def lookdeep ( start = -1 , flag = False , se = None ) :

    look_query_lt = query_lt [ start + 1 : ]

    # ( pos , val )
    deep_se =  se_lt [ -1 ]
    depth = 0
    for x in se_lt:
        if flag :
            if se == x :
                continue
        if x not in look_query_lt :
            return x
        for z in enumerate ( look_query_lt ) :
            if z [ 1 ] == x :
                if z [ 0 ] >= depth :
                    depth = z [ 0 ]
                    deep_se = x 
                break

    return deep_se



file_contents = open ( 'input_large.txt' ) 

file_write = open ( 'output.txt' , 'w+' )

test_case = int ( file_contents.readline ( ) )


cnt = 0 
cnt1 = 0 


while cnt < test_case :
    
    se = int ( file_contents.readline ( ) )

    se_lt = [ ]

    flag_lt = [ ]

    cnt1 = 0

    while cnt1 < se :
        se_lt.append ( file_contents.readline ( ) )
        flag_lt.append ( False )
        cnt1 += 1

    query =  int ( file_contents.readline ( ) )

    query_lt = [ ]

    cnt2 = 0

    while  cnt2 < query :
        query_lt.append ( file_contents.readline ( ) ) 
        cnt2 += 1


    start_se = None

    for x in se_lt :
        if x not in query_lt :
            start_se = x 
            break

    if not start_se :
                start_se = lookdeep (  ) 

    switch = 0 

    for x in enumerate ( query_lt ) :
        if start_se == x [ 1 ]:
            start_se = lookdeep ( start = x [ 0 ] , flag = True , se = x [ 1 ] ) 
            switch += 1
#        print x , start_se.strip ( )  , switch 
        
    file_write.write ( "Case #%d: %d\n" %( cnt + 1 , switch ) )
    
    cnt += 1             
