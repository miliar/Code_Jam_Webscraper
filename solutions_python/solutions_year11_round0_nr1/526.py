def solve(n,p):
	count=0
	oPos=1
	bPos=1
	lastMovesO=0
	lastMovesB=0
	for i in range(n):
		if p[i*2]=='O':
			pos=int(p[i*2+1])
			#print 'O go to %d from %d' %(pos, oPos)
			movesO = abs(oPos-pos)
			additionalMoves=movesO-lastMovesB
			#print('movesO ',movesO, 'lastMovesB ',lastMovesB,'additionalMoves of O: ',additionalMoves)
			if additionalMoves>0:
				count=count+additionalMoves
				lastMovesO = lastMovesO+additionalMoves+1
			else:
				lastMovesO = 1
			lastMovesB=min(0,abs(lastMovesB-movesO-1))
			count=count+1
			lastMovesB=0
			oPos=pos
			#print 'count: ',count ,' lastMovesO: ',lastMovesO,' lastMovesB: ',lastMovesB
		else:
			pos=int(p[i*2+1])
			#print 'B go to %d from %d' %(pos, bPos)
			movesB = abs(bPos-pos)
			additionalMoves=movesB-lastMovesO
			#print('movesB ',movesB, 'lastMovesO ',lastMovesO,'additionalMoves of B: ',additionalMoves)
			if additionalMoves>0:
				count=count+additionalMoves
				lastMovesB = lastMovesB+additionalMoves+1
			else:
				lastMovesB = 1
			lastMovesO=min(0,abs(lastMovesO-movesB-1))
			count=count+1
			lastMovesO=0
			bPos=pos
			#print('count: ',count ,' lastMovesB: ',lastMovesB,' lastMovesO: ',lastMovesO)
	return count

#main
from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, input.readline().rstrip('\n').split(' '))
    start_time=time()
    output = open('c:/gcj/output', 'w')
    input = open("c:/gcj/in.txt", "r")
    T = int(input.readline())
    for case in range(1, T + 1):
        rInput=input.readline().rstrip('\n').split(' ')
        ans = solve(int(rInput[0]),rInput[1:])
        s = "Case #%d: %d\n"%(case, ans)
        print s,
        output.write(s)
    print "Total time: %d msec"%(1000*(time()-start_time))