import sys

f = open(sys.argv[1])
f2 = open('res.text', "w")



for i in range(int(f.readline().strip())):
	N = f.readline()
	arr = map(int, f.readline().strip().split(" "))
	sum_diff = 0
	min_diff = 0
	for index, num in enumerate(arr[1:]):
		sum_diff -= min(0, num - arr[index])
		min_diff = min(min_diff, num - arr[index])
	crate = 0
	for num in arr[:-1]:
		crate += min(-min_diff, num)

	f2.write("Case #{n}: {a} {b}\n".format(a=sum_diff, b=crate, n=i+1))
