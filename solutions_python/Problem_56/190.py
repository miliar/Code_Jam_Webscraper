import sys
import os
import math
import copy


#------------------------------
# debug
en_debug = 1
en_debug = 0

def debug(*s):
    if( en_debug):
        print(*s)
#------------------------------




#------------------------------
# main
#------------------------------

#get input from file if file exists
file_name='d.txt'
file_name='A-small-attempt0.in'
if os.path.exists(file_name) :
    fp = open(file_name,"r")
    if fp:
        sys.stdin = fp

#start working
N = int(sys.stdin.readline().strip())
debug ( 'case num = ',N )

for qw in range(1, N+1):
    #get N K
    n_k =  (sys.stdin.readline().strip()).split(" ")
    debug( n_k )
    N=int( n_k[0] )
    K=int( n_k[1] )
    debug( N,K )

    #get map
    map=[]
    for i in range(N):
        row = list(sys.stdin.readline().strip())
        map.append(row)
        debug(row)
    #debug(map)

    #rotate
    new_map=copy.deepcopy(map)
    #debug( 'new map =',new_map )

    for y in range(N):
        in_pos = N-1
        for x in range(N-1,-1,-1):
            debug('x=',x,' y=',y,' in_pos=',in_pos)
            if ( map[y][x] != '.' ):
                new_map[y][x] = '.' 
                new_map[y][in_pos] = map[y][x]
                in_pos = in_pos-1
    #print( new_map )

    #check result
    b_ok=0
    r_ok=0
    #check v 
    for y in range(N):
        b_num=0
        r_num=0
        last_p=' '
        for x in range(N):
            if( new_map[y][x] == 'B' ):
                if( last_p != 'B' ):
                    b_num = 1
                else:
                    b_num+=1
            if( new_map[y][x] == 'R' ):
                if( last_p != 'R' ):
                    r_num = 1
                else:
                    r_num+=1
            last_p= new_map[y][x]
        debug( 'b_num=', b_num,' r_num=',r_num )
        if( b_num >= K ): b_ok = 1
        if( r_num >= K ): r_ok = 1

    #check h
    if( b_ok*r_ok == 0 ):
        for x in range(N):
            b_num=0
            r_num=0
            last_p=' '
            for y in range(N):
                if( new_map[y][x] == 'B' ):
                    if( last_p != 'B' ):
                        b_num = 1
                    else:
                        b_num+=1
                if( new_map[y][x] == 'R' ):
                    if( last_p != 'R' ):
                        r_num = 1
                    else:
                        r_num+=1
                last_p= new_map[y][x]
            debug( 'b_num=', b_num,' r_num=',r_num )
            if( b_num >= K ): b_ok = 1
            if( r_num >= K ): r_ok = 1

    #check left 
    if( b_ok*r_ok == 0 ):
        for i in range(2*N-1):
            b_num=0
            r_num=0
            debug( '....................' )
            last_p=' '
            for row in range(i+1):
                col=i-row
                if( col<N and  col>=0 and row<N ):
                    debug( '(',col,',',row,')' )
                    if( new_map[col][row] == 'B' ):
                        if( last_p != 'B' ):
                            b_num = 1
                        else:
                            b_num+=1
                    if( new_map[col][row] == 'R' ):
                        if( last_p != 'R' ):
                            r_num = 1
                        else:
                            r_num+=1
                    last_p= new_map[col][row]
            debug( 'b_num=', b_num,' r_num=',r_num )
            if( b_num >= K ): b_ok = 1
            if( r_num >= K ): r_ok = 1

    debug( '=============')
    #check right
    if( b_ok*r_ok == 0 ):
        for i in range(2*N-1):
            b_num=0
            r_num=0
            debug( '....................' )
            last_p=' '
            for row in range(i+1):
                col=i-row
                if( col<N and  col>=0 and row<N ):
                    row = N-row-1
                    debug( '(',col,',',row,')' )
                    if( new_map[col][row] == 'B' ):
                        if( last_p != 'B' ):
                            b_num = 1
                        else:
                            b_num+=1
                    if( new_map[col][row] == 'R' ):
                        if( last_p != 'R' ):
                            r_num = 1
                        else:
                            r_num+=1
                    last_p= new_map[col][row]
            debug( 'b_num=', b_num,' r_num=',r_num )
            if( b_num >= K ): b_ok = 1
            if( r_num >= K ): r_ok = 1

    if( b_ok and r_ok ): result='Both' 
    if( not b_ok) and ( not r_ok ): result='Neither' 
    if( b_ok )and (not r_ok ): result='Blue' 
    if( not b_ok )and (r_ok ): result='Red' 
    print( 'Case #%d:' % qw,result )

#ending
sys.stdin=sys.__stdin__
#a=input("pausing...")
