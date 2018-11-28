import operator



def next_stall(stalls):
	stall_lists = stalls.split("0")
	lens = []
	for stall_list in stall_lists:
		lens.append(len(stall_list))

	max_i, max_v = max(enumerate(lens), key=operator.itemgetter(1))
	ls = max_v / 2 if max_v % 2 != 0 else (max_v / 2) - 1
	lr = max_v / 2
	stall_lists[max_i] = stall_lists[max_i][:ls]+"0"+stall_lists[max_i][ls+1:]

	return min(ls,lr), max(ls,lr), '0'.join(stall_lists)



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, k = [int(s) for s in raw_input().split(" ")]
	stalls = "x"*n

	for j in range(k):
		min_s, max_s, stalls = next_stall(stalls)
		#print stalls

	print "Case #{}: {} {}".format(i, max_s, min_s)







"""
4 2
 1234
0xxxx0

1 Ls = 0, Rs = 3  0, 3 
2 Ls = 1, Rs = 2  1, 2
3 Ls = 2, Rs = 1  1, 2
4 Ls = 3, Rs = 0  0, 3
0x0xx0


1 Ls = 0, Rs = 0  0, 0
3 Ls = 0, Rs = 1  0, 1
4 Ls = 1, Rs = 0  0, 1
0x00x0

------------------------
0xxxxx0
1 0,4
2 1,3
3 2,2 <
4 3,1
5 4,0

0xx0xx0

"""


