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

starts = time.time()

# ------------------------------------------------------- 

'''
One line with two integers: N, the number of cities with horses, and Q, the number of pairs of stops we are interested in. Cities are numbered from 1 to N.
N lines, each containing two integers Ei, the maximum total distance, in kilometers, the horse in the i-th city can go and Si, the constant speed, in kilometers per hour, at which the horse travels.
N lines, each containing N integers. The j-th integer on the i-th of these lines, Dij, is -1 if there is no direct route from the i-th to the j-th city, and the length of that route in kilometers otherwise.
Q lines containing two integers Uk and Vk, the starting and destination point, respectively, of the k-th pair of cities we want to investigate.
'''

n=3
q=1

e=[]
s=[]
d= [ [ -1 for i in range(n) ] for j in range(n) ]

dest=0
done={}

def solve( city, left, speed ):
    #print hd,ad,hk,ak,turn
    #raw_input()

    if left<0: return 10**20
    if city==dest: return 0

    if (city, left, speed) in done:
        return done[ (city, left, speed) ]

    done[ (city, left, speed) ] = 10**20

    best=10**20

    for next in range(1,n+1):
        dist=d[city][next] 
        if dist != -1:
            cost= dist/speed + solve( next, left-dist, speed )
            best=min( best, cost )

            cost= dist/s[city] + solve( next, e[city]-dist, s[city] )
            best=min( best, cost )

    #print city, left, speed, '-->', best
    done[ (city, left, speed) ] = best
    return best

#test=map( int, "1 2 3".split() )
#print solve( 11, 5, 16, 5, 0 )
#print solve( 2, 1, 5, 1, 0 )
#sys.exit(0)


# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    n,q=map( int, lines[k].split() ); k+=1
    e=[-1]
    s=[-1]
    d= [ [ -1 for i in range(n+1) ] for j in range(n+1) ]

    for i in range(n):
        #print k,'--',lines[k].strip()
        #try:
        ee,ss=map( float, lines[k].split() ); k+=1
        #except:
        #    print k,lines[k]
        e.append(ee)
        s.append(ss)

    for i in range(n):
        dd=map( float, lines[k].split() ); k+=1
        for j in range(n):
            d[i+1][j+1]=float(dd[j])
        #print dd

    #print e,s,d
    
    u=[-1]
    v=[-1]
    for i in range(q):
        uu,vv=map( int, lines[k].split() ); k+=1
        u.append(uu)
        v.append(vv)

    #print u,v
    #print

    
    if case>=case_start and case<=case_end:
        ans=''
        done={}
        for j in range(1,q+1):
            start=u[j]
            dest=v[j]

            done={}
            best=10**20
            for i in range(1,n+1):
                if start!=i:
                    if d[start][i] != -1:
                        cost= d[start][i]/s[start] + solve( i, e[start]-d[start][i], s[start] )
                        #print '\t', i, cost
                        best=min( best, cost )
            #print best
            ans+=str(best)+' '

        log( 'Case #%d: %s' % (case,ans.strip()) )
    
    case+=1
    #raw_input()
    

elapsed = time.time() - starts
print 'elapsed', elapsed

'''

'''
