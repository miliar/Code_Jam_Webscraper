



def parseEngines(input_f):
	E_n=int(input_f.readline())
	engines=[]
	for i in range(E_n):
		engine=input_f.readline().strip()
		engines.append(engine)
		
	return engines
	
def parseQueries(input_f):
	Q_n=int(input_f.readline())
	
	queries=[]
	previous_query=None
	
	for i in range(Q_n):
		query=input_f.readline().strip()
		if previous_query==query:
			continue
		queries.append(query)
		previous_query=query
		
	
	return queries
	
def init_search_dict(engines):
	dict={}
	for next_engine in engines:
		dict[next_engine]=False
	return dict	





def findswitch(engines,queries,n,current_engine,state_tree):
	
	
	key=(n,current_engine)
	
	if state_tree.states.has_key(key):
		more_switch_count=state_tree.states[key]
	else:
		s=len(queries)
		print "n is",n,queries[n:],current_engine
		for i in range(n,len(queries)):
			next_q=queries[i]
			print next_q,
			if next_q==current_engine:
				s=i
				break
		print
		print "s is",s,current_engine
		if s<len(queries):
			more_switch_count=1
			
			
			smallest=10000
			for next in engines:
				if next!=current_engine:
					x=findswitch(engines,queries,s,next,state_tree)
					if x<smallest:
						smallest=x
						
			print "small is", smallest
			
			print "sss"
			more_switch_count+=smallest
		else:
			more_switch_count=0
		
		state_tree.states[key]=more_switch_count		
					
	if n==0:
		if more_switch_count<state_tree.smallest_switch:
			state_tree.smallest_switch=more_switch_count
		return more_switch_count
	else:
		return more_switch_count
	
class stree:
	def __init__(self):
		self.states={}
		self.smallest_switch=10000		
	
def myfindswitch(engines,queries):
	state_tree=stree()
	for next in engines:
		findswitch(engines,queries,0,next,state_tree)
	
	return state_tree.smallest_switch
	


def main_solve():
	import sys
	
	sys.stdout=open("debug.output","w")
	
	input_f=open(sys.argv[1],"r")
	first_line=input_f.readline()
	case_num=int(first_line)
	result_f=open("result.output","w")
	
	
	for i in range(case_num):
		engines=parseEngines(input_f)
		queries=parseQueries(input_f)
		count=myfindswitch(engines,queries)
	
		print "Case ",i+1	
		result_f.write("Case #%d: "%(i+1))
		result_f.write("%d\n"%count)
		print "count is ",count
		print
		i+=1
	
	
	    
	
	
main_solve()