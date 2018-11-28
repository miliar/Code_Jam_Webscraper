import os, time, sys

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
            outpath=f.split( '_' )[0] + '_output_%d_%d.txt' % (case_start, case_end)
            print f, '-->', outpath
            output=open( os.path.join( cur_dir, outpath ), 'w' )
            break

start = time.time()

# ------------------------------------------------------- 

k=3
#p=list( '---+-++-' )
p=list( '---------' )
n=len(p)
best=n

def flip(i):
    for j in range(i,i+k):
        if p[j]=='-': p[j]='+'
        else: p[j]='-'

def solve( i, f ):
    global best

    if i==n:
        return

    if f >= best: return

    #print p, i, f

    if not ( '-' in p ):
        best=f
        #print p, i, f, '*'*10
        return

    solve( i+1, f )

    if i+k <= n:
        flip(i)
        solve(i+1,f+1)
        flip(i)

'''
solve( 0,0 )
print best
sys.exit(0)
'''

# ------------------------ main ------------------------------- 
kk=1
case=1

while kk<len(lines):
    #n=int(lines[k]); k+=1
    t=lines[kk].split(); kk+=1
    k=int( t[1] )
    p=list( t[0] )
    n=len(p)
    best=n+1

    if case>=case_start and case<=case_end:
        solve( 0,0 )
        if best>n:
            log( 'Case #%d: IMPOSSIBLE' % (case) )
        else:
            log( 'Case #%d: %d' % (case,best) )
    
    case+=1

elapsed = time.time() - start
print '\n\t elapsed', elapsed

'''

'''
