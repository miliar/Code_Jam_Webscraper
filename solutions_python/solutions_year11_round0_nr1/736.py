def test( line ):
    arr = line.rstrip().split(' ')
    need_pressed = int( arr[0] )
    ob = []
    bb = []
    co = []
    cb = []
    prev_o = 1 
    prev_b = 1 
    for i in range( 1, len( arr ), 2 ):
        if arr[i] == 'O':
            ob.append( int( arr[i+1] ) )
        elif arr[i] == 'B':
            bb.append( int( arr[i+1] ) )
        else:
            print "error1"
            
    for i in range(0, len( ob ) ):
        co.append( abs( ob[i] - prev_o ) )
        prev_o = ob[i]
    for i in range(0, len( bb ) ):
        cb.append( abs( bb[i] - prev_b ) )
        prev_b = bb[i]
    oi = 0
    bi = 0
    bpushed = 0
    opushed = 0
    elapsed = 0
    for i in range( 1, len( arr ), 2 ):
        cost = 0
        if arr[i] == 'O':
            if co[oi] > elapsed - opushed:
                cost = co[oi] - elapsed + opushed
            elapsed += cost + 1
            oi += 1
            opushed = elapsed
        elif arr[i] == 'B':
            if cb[bi] > elapsed - bpushed:
                cost = cb[bi] - elapsed + bpushed
            elapsed += cost + 1
            bi += 1
            bpushed = elapsed
        else:
            print "error2"
    
    return elapsed 

file = []
for line in open( 'sample.txt', 'r' ):
    file.append( line )
fout = open("output.txt", "w")
ntest = int( file[0] )
for i in range( 1, ntest+1):
    elapsed = test( file[i] )
    fout.write( "Case #"+str(i)+": "+str(elapsed)+"\n" )
