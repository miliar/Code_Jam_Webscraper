#! /usr/bin/env python

def get_sq_lines( cls, start ):
    s_line_start = start
    s_length     = int( cls[ s_line_start ] )
    s_line_end   = s_line_start + s_length + 1
    q_line_start = s_line_end
    q_length     = int( cls[ q_line_start ] )
    q_line_end   = q_line_start + q_length + 1
    sls = cls[ s_line_start: s_line_end ]
    qls = cls[ q_line_start: q_line_end ]
    newstart = start + len( sls ) + len( qls )
    return [ newstart, sls, qls ]

def central( slines, qlines ):
    lint = compress2int( slines, qlines )
    n_engine = int( slines[0] )
    #print lint, ",", n_engine
    n_switch = shortest( lint, n_engine )
    return n_switch

def shortest( lint, n_engine ):
    hits = [ 0 ] * n_engine
    n_switch = 0
    for i in range( len( lint ) ):
        ci = lint[i]
        hits[ci] = 1
        if sum( hits ) == n_engine:
            hits = [ 0 ] * n_engine
            hits[ci] = 1
            n_switch = n_switch + 1
    return n_switch

def compress2int( slines, qlines ):
    n_engine = int( slines[0] )
    n_query  = int( qlines[0] )
    if n_query == 0:
        return [-1]
    l = []
    engines = slines[1:]
    for e in qlines[1:]:
        if e in slines:
            l.append( engines.index( e ) )
    lint = [ l[0] ]
    for i in l[1:]:
        if i == lint[-1]:
            pass
        else:
            lint.append( i )
    return lint

def main():
    import sys
    argv = sys.argv
    fin = argv[1]
    f = file( fin )
    ls = f.readlines()
    ls = [ s.strip() for s in ls ]
    f.close()
    nc = int( ls[0] )
    start = 1
    for i in range( nc ):
        start, slines, qlines = get_sq_lines(ls,start)
        #for l in slines: print l
        #for l in qlines: print l
        n_switch = central( slines, qlines )
        print "Case #%i: %i" %( i+1, n_switch )
    return

if __name__ == "__main__":
    main()

