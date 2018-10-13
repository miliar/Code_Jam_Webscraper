def main(data):
	N = data[0]
	K = data[1]
	d = dict()
	d[N] = 1
	temp_list = [N]
	i = 0
	req = K
	#there is no direct relation between curr and req.
	while req > 0:
		curr = temp_list[i]
		if curr < 1:
			#print d
			return [0,0]
		req -= d[curr]
		val1 = (curr)/2
		val2 = (curr-1)/2
		if val1 in d:
			d[val1]+=d[curr]
		else:
			d[val1] = d[curr]
			temp_list.append(val1)
		if val2 in d:
			d[val2]+=d[curr]
		else:
			d[val2] = d[curr]
			temp_list.append(val2)
		i+=1
	#print d
	return [val1,val2]


T = input()
for i in range(T):
	data = map(int,raw_input().split())
	result = main(data)
	print "Case #"+str(i+1)+":",result[0],result[1]
