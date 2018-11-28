def read_input( filename ):
    with open( filename, 'r' ) as f:
        lines = [ x.strip() for x in f.readlines() ]
    return lines
    
def solve1( ary, k ):
    def switch( idx ):
        for j in range( k ):
            if ary[idx+j] == '+':
                ary[idx+j] = '-'
            else:
                ary[idx+j] = '+'
    
    count = 0
    n = len( ary )
    for i in range( n ):
        if ary[i] == '-' and i <= n - k:
            switch( i )
            count += 1
    
    for i in range( n-k, n ):
        if ary[i] == '-':
            return 'IMPOSSIBLE'
    return str( count )


def ex1( f_in, f_out ):
    lines = read_input( f_in )
    with open( f_out, 'w' ) as f:
        T = int( lines[0] )
        for case in range(T):
            s, k = lines[1+case].split( ' ' )
            ary = [ s[i] for i in range(len(s)) ]
            k = int(k)
            f.write( "Case #{}: {}".format( case+1, solve1( ary, k ) ) )
            if case < T-1:
                f.write( "\n" )
                
                
ex1( "A-large.in", "A-large.out" )