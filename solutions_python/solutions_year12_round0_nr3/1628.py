import re
def recycled_numbers(n, m):

	ns = str(n)
	newn = re.sub('^0+','',ns)
	ms = str(m)
	newm = re.sub('^0+','',ms)

	return newm in (newn+newn)



def Count(a, b):
	n = a
	count = 0
	for n in range(a,b):
		for m in range(n+1,b+1):
			if recycled_numbers(n,m):
				count += 1
	
	return count

def main():
	fp = open('C-small-attempt0.in')
	out = open('output3','w')
	data = fp.read()
	cases = data.split('\n')
	n = int(cases[0])
	del cases[0]

	for i in range(n):
		nums = cases[i].split(' ')
		a = int(nums[0])
		b = int(nums[1])
		print a,' ',b
		out.writelines('Case #'+str(i+1)+': '+ str(Count(a,b))+'\n')
	fp.close()
	out.close()

if __name__ == '__main__':
	main()
