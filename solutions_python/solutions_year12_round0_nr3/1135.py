#task 4
import math

f = open('res.txt','w')
task = open('C-small-attempt0.in','r')

def test_in(ident):
	res = 0
	not_use = [False for i in range(len(ident))]
	for i in range(len(ident)):
		if not_use[i]: continue
		arr_1 = ident[i]
		tmp_res = 1
		for j in range(i+1,len(ident)):
			if not_use[j]: continue
			arr_2 = ident[j]
			for k in (range(len(arr_2))):
				if arr_1 == arr_2[k:] + arr_2[:k]:
					tmp_res+=1
					not_use[j] = True
					break
		if tmp_res != 1:
			tmp_res = math.factorial(tmp_res)//(2 * math.factorial(tmp_res-2))
			res += tmp_res
	return res


T = int(task.readline())
for it in range(T):
	nums = task.readline().split(' ')
	a = int(nums[0])
	b = int(nums[1])

	H = {}

	for i in range(a,b+1):
		arr = []
		num = i
		while num!=0:
			arr.append(num%10)
			num//=10
		sarr = str(sorted(arr))
		if sarr in H:
			H[sarr].append(arr)
		else:
			H[sarr] = [arr]

	res = 0

	for j in H:
		res += test_in(H[j])

	f.writelines('Case #' + repr(it+1) + ': ' + repr(res) + '\n')

f.close()
task.close()