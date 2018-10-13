ifile = open ( 'tmo1.txt' )

ofile = open ( 'tmo_out1.txt' , 'w+' )


tc = int ( ifile.readline ( ) )


cnt = 0

while cnt < tc :


        lt = ifile.readline ( ).split ( )


        max = int ( lt [ 0 ] )

        keys = int ( lt [ 1 ] )


        lt = ifile.readline ( ).split ( )

        lt1 = [ ]


        for x in lt :
                lt1.append ( int ( x ) )


        lt1.sort ( )
        lt1.reverse ( )

        cnt1 = 0

        press = 0

        lt2 = [ ]

        while cnt1 < max :

                lt2 = lt1 [ : keys ]

                lt1 = lt1 [ keys : ]

                for x in lt2 :

                        press += ( cnt1 + 1 ) * x

                cnt1 += 1

        l = len ( lt1 )


        if l == 0 :
                #print "Case #%d: %d" %(cnt + 1 , press )
                ofile.write ( "Case #%d: %d\n" %(cnt + 1 , press ) )

        else :
                #print "Case #%d: IMPOSSIBLE" % ( cnt + 1 )
                ofile.write ( "Case #%d: IMPOSSIBLE\n" % ( cnt + 1 ) )

        cnt += 1
        




