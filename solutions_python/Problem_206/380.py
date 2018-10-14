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

'''
b+t*s = d
t = (d-b)/s

s*t=d
s=d/t
'''

d,n=0,0
k=[]
s=[]

def solve():

    slow=0
    for i in range(n):
        b=k[i]
        r=s[i]
        dur=(d-b)/r
        #print 'dur', dur
        slow=max(slow,dur)

    ann=d/slow
    #print d,slow,ann

    return ann

'''
test=map( int, "1 2 3".split() )
print solve( test )
sys.exit(0)
'''

# ------------------------ main ------------------------------- 
kk=1
case=1

while kk<len(lines):
    d,n=map( int, lines[kk].split() ); kk+=1
    k=[]
    s=[]
    for i in range(n):
        tok=map( float, lines[kk].split() ); kk+=1
        k.append( tok[0] )
        s.append( tok[1] )

    if case>=case_start and case<=case_end:
        ans=str(solve())
        log( 'Case #%d: %s' % (case,ans) )
        #print
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
