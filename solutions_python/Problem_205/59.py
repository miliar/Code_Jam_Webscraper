import os, time, sys

sys.setrecursionlimit(1800000)
case_start, case_end = 1, 100

cur_dir=os.path.dirname( os.path.abspath(__file__) )
output=None

def log( msg ):
    print msg
    output.write( msg + '\n' )

lines=[]
for f in os.listdir( cur_dir ):
    if f.lower().endswith( '.in' ):
        if not 'output' in f:
            lines=open( os.path.join( cur_dir, f ), 'r' ).readlines()
            outpath=f.split( '.' )[0] + '_output_%d_%d.txt' % (case_start, case_end)
            print f, '-->', outpath
            output=open( os.path.join( cur_dir, outpath ), 'w' )
            break

start = time.time()

# ------------------------------------------------------- 

n=-1

B=1
D=1
HD=2

done={}

def solve( hd,ad,hk,ak, turn ):
    #print hd,ad,hk,ak,turn
    #raw_input()

    if hk<=0: return 0

    if turn:
        return solve( hd-ak,ad,hk,ak, 1-turn )

    if hd<=0: return 999999

    if ad>=hk: return 1

    #'''
    if (hd,ad,hk,ak) in done:
        return done[ (hd,ad,hk,ak) ]
    #'''

    #d=done.get( (hd,ad,hk,ak), 999999 )
    #if d<999999: return d
    done[ (hd,ad,hk,ak) ] = 999999

    #best=999999
    a=solve( hd,ad,hk-ad,ak, 1-turn )
    b=solve( hd,ad+B,hk,ak, 1-turn )
    c=solve( HD,ad,hk,ak, 1-turn )
    d=solve( hd,ad,hk,max(0,ak-D), 1-turn )
    best=1+min( 999999, a, b, c, d )
    #print hd,ad,hk,ak,best
    done[ (hd,ad,hk,ak) ] = best
    #raw_input()

    return best

#test=map( int, "1 2 3".split() )
#print solve( 11, 5, 16, 5, 0 )
#print solve( 2, 1, 5, 1, 0 )
#sys.exit(0)


# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    hd,ad,hk,ak,B,D=map( int, lines[k].split() ); k+=1
    HD=hd
    done={}

    if case>=case_start and case<=case_end:
        ans=solve( hd,ad,hk,ak,0 )
        if ans<999999:
            log( 'Case #%d: %d' % (case,ans) )
        else:
            log( 'Case #%d: IMPOSSIBLE' % (case) )
    
    case+=1
    #raw_input()

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
