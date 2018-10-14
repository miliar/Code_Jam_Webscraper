INPUT_FILE = 'B-small-attempt1.in'
#INPUT_FILE = 'test.in'
OUTPUT_FILE = 'B-small-attempt1_out.txt'
import math
# Python program to find maximal Bipartite matching. 
class Graph:
    def __init__(self,graph):
        self.graph = graph # residual graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])
 
    # A DFS based recursive function that returns true if a
    # matching for vertex u is possible
    def bpm(self, u, matchR, seen):
 
        # Try every job one by one
        for v in range(self.jobs):
 
            # If applicant u is interested in job v and v is
            # not seen
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True # Mark v as visited
 
                '''If job 'v' is not assigned to an applicant OR
                previously assigned applicant for job v (which is matchR[v]) 
                has an alternate job available. 
                Since v is marked as visited in the above line, matchR[v] 
                in the following recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False
 
    # Returns maximum number of matching 
    def maxBPM(self):
        '''An array to keep track of the applicants assigned to
        jobs. The value of matchR[i] is the applicant number
        assigned to job i, the value -1 indicates nobody is
        assigned.'''
        matchR = [-1] * self.jobs
        result = 0 # Count of jobs assigned to applicants
        for i in range(self.ppl):
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs
            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result

def getCounts(elem, ingr):
	ratio = elem * 1.0 / ingr
	lowerb = int(math.ceil(ratio/1.1)+0.1)
	upperb = int(ratio/0.9)
	if lowerb <= upperb:
		return (lowerb, upperb)
	return None
		
def eliminateImpossibles(lst,ingr):
	lstnew = []
	for elem in lst:
		counts = getCounts(elem, ingr)
		if(counts):
			lstnew += [elem]
	return lstnew
				
def solve(f_in):
	l = f_in.readline().strip()
	lst = l.split(' ')
	N = int(lst[0])
	P = int(lst[1])
	l = f_in.readline().strip()
	lst = l.split(' ')
	ingr = map(lambda x: int(x), lst)
	Q = []
	for i in range(N):
		l = f_in.readline().strip()
		lst = l.split(' ')
		Q.append(map(lambda x: int(x), lst))
	if N == 1:
		return len(eliminateImpossibles(Q[0],ingr[0]))
	elif N == 2:
		graph=[]
		for i in range(P):
			graph += [[0]*P]
		for i in range(P):
			for j in range(P):
				elem = Q[0][i]
				elemB = Q[1][j]
				c1 = getCounts(elem, ingr[0])
				c2 = getCounts(elemB, ingr[1])
				if not c1 or not c2:
					continue
				#print "CountA", c1
				#print "CountB", c2
				if (c1[1] >= c2[0] and c1[1] <= c2[1]) or (c1[0] >= c2[0] and c1[0] <= c2[1]) or (c1[1] >= c2[1] and c1[0] <= c2[0]):
					graph[i][j] = 1
				#print "Graph", graph
		#print graph
		g = Graph(graph)
		return g.maxBPM()
	return 0

with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline())
		for i in range(T):
			f_out.write('Case #%d: %d\n'%(i + 1, solve(f)))
				