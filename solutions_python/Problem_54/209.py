"""
Fair Warning
By Xiao
"""
import sys
def gcd(i,j):
	if (i > j):
		temp = i
		i = j
		j = temp
	if i == 0:
		return j
	if (i == j):
		return i
	return gcd(i, j % i)
	
def Solve(tList):
	deltaList = []
	for i in range(len(tList) - 1):
		deltaList.append(abs(tList[i+1] - tList[i]))
	
	maxgcd = deltaList[0]
	for i in deltaList[1:]:
		maxgcd = gcd(maxgcd,i)
	
	mod = tList[0] % maxgcd
	for i in tList[1:]:
		if (i % maxgcd != mod):
			print 'ooops, wrong algorithms'
			return
	
	y = (maxgcd - mod) % maxgcd
	return y

if __name__ == "__main__":
	input_file = open(sys.argv[1])
	output_file = open(sys.argv[2],'w')
	t = int(input_file.readline())
	for i in range(t):
		ss = input_file.readline()
		li = [int(x) for x in ss.split(' ')]
		li = li[1:]
		res = Solve(li)
		output_file.write('Case #' + str(i+1) + ': ' + str(res) + '\n')

	input_file.close()
	output_file.close()
