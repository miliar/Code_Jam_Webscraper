'''
Deterministic Rules:
Choose any S that:
1. makes min(ls,rs) maximum
2. makes max(ls,rs) maximum\
3. the leftmost
'''

def fbi(left,right): # return best point in range(left index, right index)
	i=(left+right)//2
	li=i-left-1
	ri=right-i-1
	return (i,min(li,ri),max(li,ri))

def main(n,k):
	if n==k:
		return (0,0)
	rec=[]
	for i in range(n+2):
		rec.append(0)
	rec[0]=1
	rec[n+1]=1
	for j in range(1,k+1):
		lb=0
		rb=1
		candidate=[]
		while rb<=n+1:
			while rec[rb]==0 and rb<=n+1:
				rb=rb+1
			if lb==rb-2:
				candidate.append((lb+1,0,0))
			elif lb==rb-3:
				candidate.append((lb+1,0,1))
			elif lb==rb-4:
				candidate.append((lb+2,1,1))
			elif lb!=rb-1:
				candidate.append(fbi(lb,rb))
			lb=rb
			rb=rb+1
		min_v=0
		max_v=0
		for (index,min_d,max_d) in candidate:
			if min_d>min_v:
				min_v=min_d
			if max_d>max_v:
				max_v=max_d
		what_are_mins=[]
		for (index,min_d,max_d) in candidate:
			if min_d==min_v:
				what_are_mins.append((index,min_d,max_d))
		if len(what_are_mins)==1:
			rec[what_are_mins[0][0]]=1
			last=(what_are_mins[0][1],what_are_mins[0][2])
		else:
			what_are_maxs=[]
			for (index,min_d,max_d) in what_are_mins:
				if max_d==max_v:
					what_are_maxs.append((index,min_d,max_d))
			if len(what_are_maxs)==1:
				rec[what_are_maxs[0][0]]=1
				last=(what_are_maxs[0][1],what_are_maxs[0][2])
			else:
				min_index=n+1
				for (index,min_d,max_d) in what_are_maxs:
					if min_index>index:
						min_index=index
						last=(min_d,max_d)
				rec[min_index]=1
	return last



t = int(input())
for i in range(1, t + 1):
	n, m = [int(s) for s in input().split(" ")]
	result=main(n,m)
	print("Case #%d: %d %d" %(i, result[1], result[0]))


