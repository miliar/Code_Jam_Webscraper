import os, time, sys
sys.setrecursionlimit(1800000)
cur_dir=os.path.dirname( os.path.abspath(__file__) )
output=open( os.path.join( cur_dir, 'output.txt' ), 'w' )

def log( msg ):
    print msg
    output.write( msg + '\n' )

def log2( msg ):
    #print msg
    output.write( msg + '\n' )

lines=[]
for f in os.listdir( cur_dir ):
    if f.lower().endswith( '.in' ):
        lines=open( os.path.join( cur_dir, f ), 'r' ).readlines()
        break

# ------------------------------------------------------- 

def solve(s):
	#print s
	tot=0
	ans=0
	for i in range( len(s) ):
		if tot<i:
			diff=i-tot
			ans+=diff
			tot+=diff
		tot+=int(s[i])
		#print i, s[i], tot

	return ans

#print solve( '123' )

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
	l,m=lines[k].strip().split(); k+=1
	log( 'Case #%d: %s' % (case,solve(m)) )
	#break
	case+=1
