
f = open ( 'msp_input1.txt' )
f1 = open ( 'msp_output.txt' , 'w+' )

noc = int ( f.readline ( ) )


cnt1 = 0

while cnt1 < noc :

        len = int ( f.readline ( ) )

        v1 = f.readline ( ).split ( )

        v2 = f.readline ( ).split ( )


        v3 = [ ]
        v4 = [ ]


        for x , y in zip ( v1 , v2 ) :
                v3.append ( int ( x ) )
                v4.append ( int ( y ) )

        


        v3.sort ( )
        v4.sort ( )
        v4.reverse ( )

#        print v3
#        print v4

        sum = 0

        for x , y in zip ( v3 , v4 ) :

                prod = int ( x ) * int ( y )
                sum += prod


        f1.write ( "Case #%d: %d\n" %( cnt1 + 1 , sum ) )
#        print "Case #%d = %d" %( cnt1 + 1 , sum )

        cnt1 += 1

f.close ( )
f1.close ( )






