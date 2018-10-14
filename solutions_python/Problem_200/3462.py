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

345123
344999

'''

def way1(n):
    d=[ int(x) for x in str(n) ]
    d[0]-=1
    w=str(d[0])+'9'*(len(d)-1)
    return int(w)

def fast(n):
    d=[ int(x) for x in str(n) ]
    size=len(d)
    i=0
    while i+1 < size:
        if d[i]>d[i+1]:
            break
        i+=1

    d[i]-=1
    i+=1
    while i<size:
        d[i]=9
        i+=1

    #print d
    return int( ''.join( [str(x) for x in d] ) )

def fastrep(n):
    while 1:
        if check(n): return n
        n=fast(n)

n=-1

def check(n):
    s=list(str(n))
    return s==sorted(s)

def brute( n ):
    while n:
        if check(n): break
        n-=1
    return n

def solve(n):
    print 'solve', n
    #print 'way1', way1(n)
    print 'fastrep', fastrep(n)
    print 'brute', brute(n)
    print '\n'


'''
solve( 1322 )
solve( 10111 )
solve( 33221 )
solve(32999)
solve( 45123 )


solve(11111)
solve(11110)
solve(11011)

solve(11)
solve(10)
solve(991)

sys.exit(0)
'''

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    l=lines[k].strip(); k+=1
    n=int( l );

    if case>=case_start and case<=case_end:
        ans=fastrep( n )
        log( 'Case #%d: %d' % (case,ans) )
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''

