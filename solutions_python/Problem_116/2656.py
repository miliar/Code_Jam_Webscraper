def col(matrix, i):
    return [row[i] for row in matrix]

def evalLine(L):    
    if 'X' in L and 'O' in L:
        return ""
    if 'X' in L:
        return "X won"
    else:
        return "O won"    
    
def main(A):     
    completed=True
    #horizontal
    for i in A:
        if '.' in i:            
            completed=False
            continue 
        #print i
        x=evalLine(i)
        #print x
        if x!="": return x
    #vertical
    #print "vert"
    for i in range(4):
        l=col(A,i)
        if '.' in l:            
            continue        
        x=evalLine(l)
        if x!="":
            return x
    #diagonal
    #print "d1"
    l=[A[i][i] for i in range(4)]
    #print l
    x="" if '.' in l else evalLine(l)
    if x!="":
        return x

    #print "d2"
    l=[A[3-i][i] for i in range(4)]
    x="" if '.' in l else evalLine(l)
    if x!="":
        return x

    return "Draw" if completed else"Game has not completed"


if __name__ == '__main__':
	import sys
        #print sys.stdin.readline()
	N = int(sys.stdin.readline())
	for i in xrange(N):
            A=[]
            for j in xrange(4):
		A.append(sys.stdin.readline()[:4])
            sys.stdin.readline()
            resp=main(A)
            if i==N-1:
                sys.stdout.write("Case #%d: %s" % (i + 1, resp))                
            else:
                print "Case #%d: %s" % (i + 1, resp)
