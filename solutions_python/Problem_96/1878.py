import sys

series=[ [[0,0,0]], [[0,0,1]], [[0,1,1],[0,0,2]], [[1,1,1],[0,1,2]], [[1,1,2],[0,2,2]], [[1,2,2],[1,1,3]], [[2,2,2],[1,2,3]], [[2,2,3],[1,3,3]], [[2,3,3],[2,2,4]], [[3,3,3],[2,3,4]], [[3,3,4],[2,4,4]], [[3,4,4],[3,3,5]], [[4,4,4],[3,4,5]], [[4,4,5],[3,5,5]], [[4,5,5],[4,5,6]], [[5,5,5],[4,5,6]], [[5,5,6],[4,6,6]], [[5,6,6],[5,5,7]], [[6,6,6],[5,6,7]], [[6,6,7],[5,7,7]], [[6,7,7],[6,6,8]], [[7,7,7],[6,7,8]], [[7,7,8],[6,8,8]], [[7,8,8],[7,7,9]], [[8,8,8],[7,8,9]], [[8,8,9],[7,9,9]], [[8,9,9],[8,8,10]], [[9,9,9],[8,9,10]], [[9,9,10],[8,10,10]], [[9,10,10]], [[10,10,10]] ]
xcpt=[0,1,29,30]
scores=[]*30
visited=[False]*30
total=0

def find_Comb(scores,N,S,p):
	global visited	
	i=0
	c=0
	if S==0:
		while i<N:
			if visited[i]==True:
				i=i+1
				continue
			if series[scores[i]][0][2]>=p:
				c=c+1
			i=i+1
		return c
	
	m=0
	d=0
	while d<N:
		if (scores[d]<=1 or scores[d]>=29) or visited[d]:
			d=d+1
			continue
		visited[d]=True
		if series[scores[d]][1][2]>=p:
			c=c+1
		tmp = c+find_Comb(scores,N,S-1,p)
		if tmp > m:
			m=tmp
		if series[scores[d]][1][2]>=p:
			c=c-1
		visited[d]=False
		d=d+1
	return m


def main():
	
	tc=int(raw_input())
	c=0
	while c<tc:
		c=c+1
		inp=raw_input().split()
		N=int(inp[0])
		S=int(inp[1])
		p=int(inp[2])
		scores=inp[3:]
		k=0
		for s in scores:
			scores[k]=int(s)
			k=k+1
		scores.sort()
		global total
		total=0
		#cnt = recurse(scores,N,S,0,p)
		#mmm = max(cnt,total)
		global visited
		visited=[False]*30
		mmm = find_Comb(scores,N,S,p)
		sys.stdout.write( "Case #%d: %d\n" % (c,mmm))
main()
