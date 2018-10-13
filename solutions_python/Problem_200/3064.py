def read_input( filename ):
    with open( filename, 'r' ) as f:
        lines = [ x.strip() for x in f.readlines() ]
    return lines

def solve2( ary ):
    def decr( char ):
        return chr( ord( char ) - 1 )
    n = len( ary )
    current = '0'
    flag = False
    idx, i = 0, 0
    while i < n and not flag:
        if ary[i] >= current:
            current = ary[i]
        else:
            flag = True
            idx = i
        i += 1
    if not flag:
        return ''.join( ary )
    for i in range( idx+1, n ):
        ary[i] = '9'
    while idx > 0:
        if ary[idx] < ary[idx-1]:
            ary[idx-1] = decr( ary[idx-1] )
            ary[idx] = '9'
        idx -= 1
    if ary[0] == '0':
        ary = ary[1:]
    return ''.join( ary )

def ex2( f_in, f_out ):
    lines = read_input( f_in )
    with open( f_out, 'w' ) as f:
        T = int( lines[0] )
        for case in range(T):
            s = lines[1+case]
            ary = [ s[i] for i in range(len(s)) ]
            f.write( "Case #{}: {}".format( case+1, solve2( ary ) ) )
            if case < T-1:
                f.write( "\n" )
ex2( "B-large.in", "B-large.out" )