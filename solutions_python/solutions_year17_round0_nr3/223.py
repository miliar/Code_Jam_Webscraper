f = open("C.out",'w')
tt = int(raw_input())

layerMax = [0] + [2**(i+1)-1 for i in xrange(60)]

def solution(n,leaf,layer):
	if layer == 1:
		return ((n-1)/2,(n-1)/2+(n-1)%2)
	if leaf%2 == 0:
		n = (n-1)/2
	else:
		n = (n-1)/2 + (n-1)%2
	leaf = leaf/2+leaf%2
	return solution(n,leaf,layer-1)

for t in xrange(tt):
	n,k = map(int,raw_input().split())
	layer = 1
	for i in xrange(61):
		if k<=layerMax[i]:
			layer = i
			break
	print layer
	leaf = k - layerMax[layer-1]
	answer = solution(n,leaf,layer)
	f.write("Case #{0}: {1} {2}\n".format(t+1,answer[1],answer[0]))
f.close()
