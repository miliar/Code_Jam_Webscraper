import sys

def ride(q,k):
	t=0
	i=0
	while (i<len(q)) and (t+q[i]<=k):
		t+=q[i]
		i+=1
	return i,t,q[i:]+q[0:i]

def runride(R,k,N,q):
	ringfound=0
	r=0
	total=0
	historic_indexes=[]
	historic_vals=map(lambda x:([],[]),range(N))
	cur_index=0
	ring_index=0
	ring_pair=()
	while ringfound==0 and r<R:
		new_index,value,new_q=ride(q,k)
		historic_indexes.append(cur_index)
		for j in set(historic_indexes):
			last_indexes,index_values=historic_vals[j]
			last_indexes.append(new_index)
			index_values.append(value)
			historic_vals[j]=(last_indexes,index_values)
		# if a ring exists then the sum of its indexes divides N
		ring_list=filter(lambda x:x[1]==0 and len(historic_vals[x[0]][0])>0,enumerate(map(lambda x:sum(x[0])%N,historic_vals)))
		if len(ring_list)>0:
			ringfound=1
			ring_index=ring_list[0][0]
		cur_index=(cur_index+new_index)%len(q)
		q=new_q
		r=r+1
		total=total+value
	if ringfound==1 and r<R:
		# we found a ring and there are more runs left
		# so we should find how many resulting ring-runs there are
		# and add their value (plus the remainder)
		runs=R-r
		ring_indexes,ring_values=historic_vals[ring_index]
		ring_size=len(ring_indexes)
		ring_value=sum(ring_values)
		ring_runs=runs/ring_size
		remaining_runs=runs%ring_size
		ring_runs_value=ring_runs*ring_value
		nonring_final_runs=sum(ring_values[:remaining_runs])
		total=total+ring_runs_value+nonring_final_runs
	return total

if len(sys.argv)!=2:
  print 'Usage: themepark.py <inputfile>'
  exit(1)
  
inputfile=open(sys.argv[1],'r')
outputfile=open('themepark_results.txt','w')

numoflines=int(inputfile.readline())
for i in range(numoflines):
  R,k,N=inputfile.readline().strip().split(' ')
  R=int(R)
  N=int(N)
  k=int(k)
  q=map(lambda x:int(x),inputfile.readline().strip().split(' '))
  result=runride(R,k,N,q)
  outputfile.write("Case #%d: %s\n"% (i+1,result))