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
            outpath=f.split( '.' )[0] + '_output_%d_%d.txt' % (case_start, case_end)
            print f, '-->', outpath
            output=open( os.path.join( cur_dir, outpath ), 'w' )
            break

start = time.time()

# ------------------------------------------------------- 

from sortedcontainers import SortedList

test=200
n=10000
s=SortedList()
s.update( [1, n+2] )
 
# 123456
# O.OO.O

def gap():
    lim=len(s)-1
    i=0
    #left,right=0,0
    best=-1
    besti=-1
    mid=-1

    while i<lim:
        diff=s[i+1]-s[i]
        if diff > best:
            best=diff
            besti=i
            mid=( s[i+1]+s[i] )/2
            left=mid-s[i]
            right=s[i+1]-mid
        i+=1

    return (mid, left, right)

def solve( k ):
    ans=0
    m,l,r=0,0,0

    while k:
        m,l,r = gap()
        #print list(s), k, m, l, r
        s.add( m )
        k-=1
    
    return ( max(l,r)-1, min(l,r)-1 )

'''
print solve( test )
sys.exit(0)
'''


# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    t=lines[k].split(); k+=1
    n=int( t[0] )
    q=int( t[1] )
    s=SortedList()
    s.update( [1, n+2] )

    if case>=case_start and case<=case_end:
        ans=solve( q )
        log( 'Case #%d: %d %d' % (case,ans[0],ans[1]) )
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
