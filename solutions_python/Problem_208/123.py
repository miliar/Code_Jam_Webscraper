from __future__ import division

import sys
import heapq

def compute_subtree(D, rest, speed, start, N):
	cur = [float('inf')] * N

	worklist = [(float(0),start)]

	while len(worklist) > 0:
		(d,pos) = heapq.heappop(worklist)
		if d >= cur[pos]:
			continue

		cur[pos] = d
		for j in xrange(N):
			(dp,posp) = (d + D[pos][j], j)
			#print "%s -> %s" % ((d,pos),(dp,posp))
			assert dp > d
			if dp > rest:
				continue
			elif dp < cur[posp]:
				heapq.heappush(worklist, (dp,posp))

	return [cur[i]/float(speed) for i in xrange(N)]

def shortest_path(D, start, end, N):
	cur = [float('inf')] * N

	worklist = [(float(0),start)]

	while len(worklist) > 0:
		(d,pos) = heapq.heappop(worklist)
		if d >= cur[pos]:
			continue

		cur[pos] = d
		if pos == end:
			return d

		for j in xrange(N):
			(dp,posp) = (d + D[pos][j], j)
			if dp < cur[posp]:
				heapq.heappush(worklist, (dp,posp))

	return cur[end]

def run(N,Q,E,S,D,U,V):
	sg = [None] * N
	for i in xrange(N):
		sg[i] = compute_subtree(D,E[i],S[i],i,N)

	for k in xrange(Q):
		yield shortest_path(sg, U[k], V[k], N)

def main():
	T = int(raw_input())
	for t in xrange(T):
		(N,Q) = map(int, raw_input().split())
		E = [None] * N
		S = [None] * N
		D = [None] * N
		U = [None] * Q
		V = [None] * Q

		for i in xrange(N):
			(E[i],S[i]) = map(int, raw_input().split())

		for i in xrange(N):
			D[i] = map(int, raw_input().split())
			D[i] = [float('inf') if x == -1 else float(x) for x in D[i]]

		for k in xrange(Q):
			(U[k],V[k]) = map(int, raw_input().split())
			(U[k],V[k]) = (U[k]-1,V[k]-1)

		print "Case #%d: %s" % (t+1, " ".join(["%.6f" % x for x in run(N,Q,E,S,D,U,V)]))

if __name__ == '__main__':
	main()
