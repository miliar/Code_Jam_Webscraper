from random import randint
from sys import setrecursionlimit

################################################################
####################### SOLUTION ###############################
################################################################

def dfs(ih,visited, p, K):
	visited[p] = K	
	for nbr in ih[p]:
		if visited[nbr] == K:
			return True
		else:			
			if(dfs(ih,visited,nbr,K)):
				return True
	return False


def solve(ih, N):
	visited = [0 for i in xrange(N+1)]
	visited[0] = 1
			
	for i in xrange(len(visited)):
		if(visited[i]==0):				
			if(dfs(ih, visited, i, i)):
				return "Yes\n"
				
	return "No\n"
			
	
		

################################################################
###################### UTILITIES ###############################
################################################################

def slst(lst, term='\n'):
	""" convert a list to a string on a single line on its own """
	s = str(lst[0])
	for i in lst[1:]:
		s += ' ' + str(i)
	s += term
	return s
		
#################################################################
############################### TESTS ###########################
#################################################################
	
def maketest(N):
	""" make a single test case of size N """
	ln = [N]
	for i in xrange(N):
		ln.append(randint(1,100))
	return slst(ln)
	
def maketests(fname):
	""" make a test file """
	T = 2
	N = 5	
	
	OL = [str(T)+'\n']	
	for i in xrange(T):
		OL.append(maketest(N))
		
	fout = open(fname+'.in', 'w')
	fout.writelines(OL)
	fout.close()

#################################################################
###################### INITIALIZATION ###########################
#################################################################
	
	
def init(fname):
	#Get inputs and apply algorithms
	fin = open(fname+'.in', 'r')	
	L = [map(int, x.strip().split()) for x in fin.readlines()]
	fin.close()
	
	T = L[0][0]
	
	k = 1	
	OL = []			
	for i in xrange(1,T+1):
		N = L[k][0]
		k += 1
		ih = [[]]
		for j in xrange(N):
			ih.append(L[k][1:])
			k += 1
		OL.append('Case #' + str(i) + ': ' + solve(ih,N))
		
	fout = open(fname+'.out', 'w')
	fout.writelines(OL)
	fout.close()
	
setrecursionlimit(2000)
#init('A_test')
#init('A-small-attempt1')
init('A-large')	






