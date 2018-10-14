import math

def amoeba(lst):
	res = []
	for x in lst:
		if x%2 == 0:
			res.append(math.floor(x/2))
			res.append(math.floor((x-1)/2))
		else:
			res.append(math.floor(x/2))
			res.append(math.floor(x/2))
	return res

def main():
	in_file = open('input.in', 'r')
	out_file = open('output.txt', 'w')

	inputs = in_file.readlines()

	data = {}

	T = int(inputs.pop(0).strip())

	for t in range(T):
		#print('t: %s' % (t+1))
		N,K = [int(x) for x in inputs.pop(0).strip().split()]
		if N in data.keys():
			if K > len(data[N][0]):
				times = math.floor(math.log(K,2)) + 1
				needed = times - data[N][2]
				for_data = []
				last = data[N][1]
				for i in range(needed):
					multiple = amoeba(last)
					for i in range(0,len(multiple),2):
						for_data.append((multiple[i], multiple[i+1]))
					multiple.sort(reverse=True)
					last = [x for x in multiple if x > 0]
				data[N][0].extend(for_data)
				data[N][1] = last
				data[N][2] = times
		else:
			last = [N]
			for_data = []
			times = math.floor(math.log(K,2)) + 1
			for i in range(times):
				multiple = amoeba(last)
				for i in range(0,len(multiple),2):
					for_data.append((multiple[i], multiple[i+1]))
				multiple.sort(reverse=True)
				last = [x for x in multiple if x > 0]
			data[N] = [for_data, last, times]

		out_file.write("Case #%d: %s %s\n" % (t+1, data[N][0][K-1][0], data[N][0][K-1][1]))

	in_file.close()
	out_file.close()



if __name__ == '__main__':
	main()