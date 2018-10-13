import os, time, sys
sys.setrecursionlimit(1800000)
cur_dir=os.path.dirname( os.path.abspath(__file__) )
output=open( os.path.join( cur_dir, 'output.txt' ), 'w' )

def log( msg ):
    print msg
    output.write( msg + '\n' )

lines=[]
for f in os.listdir( cur_dir ):
    if f.lower().endswith( '.in' ):
        lines=open( os.path.join( cur_dir, f ), 'r' ).readlines()
        break

# ------------------------------------------------------- 

best=2**31

def solve( cakes, cost ):
	global best
	if cost>=best: return

	#print cakes, cost
	high=max( cakes )
	if cost+high < best:
		best=cost+high
		#print 'best=', best

	if high<=2: return

	ind=cakes.index( high )
	for k in range( high/2 - 2, high/2 + 2 ):
		new_cakes=cakes[:]
		new=k #high/2
		new_cakes.append( new )
		new_cakes[ind]-=new
		solve( new_cakes, cost+1 )

#solve( [8, 90], 0 )
#print best

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
	d=lines[k].strip(); k+=1
	e=[ int(x) for x in lines[k].strip().split() ]; k+=1

	best=2**31
	solve( e, 0 )
	log( 'Case #%d: %s' % (case,best) )
	print
	case+=1
