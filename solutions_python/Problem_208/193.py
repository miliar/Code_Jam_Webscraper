def main():
	[N,Q] = map(int,raw_input().split())
	temp = list()
	distances =  [0]
	d = dict()
	for i in range(N):
		temp.append(map(int,raw_input().split()))
	for i in range(N-1):
		stream = map(int,raw_input().split())
		distances.append(distances[-1] + stream[i+1])
	stream = map(int,raw_input().split())
	dummy = raw_input()
	d[0] = 0
	for i in range(1,N):
		d[i] = 10**18
		for j in range(0,i):
			if distances[i] - distances[j] > temp[j][0]:
				continue
			else:
				d[i] = min(d[i],(distances[i] - distances[j])/1.0/temp[j][1] + d[j])
	return d[N-1]

T = input()
for i in range(T):
	res = main()
	print "Case #" + str(1+i) + ":",res
