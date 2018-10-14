def tidy(a):
	for i in range(len(a)-1):
		if(a[i]==0) or (a[i]>a[i+1]):
			return False
	return True
def remove_zeros(a):
	for i in range(len(a)):
		if a[i] != 0 :
			return a[i:]

def refine(a):
	for i in range(len(a)-1):
		if(a[i]>a[i+1]):
			res = a[:i]+[a[i]-1]+(len(a)-i-1)*[9]
			res = remove_zeros(res)
			return res
def main():
	filename = 'inB.txt'
	data =  open(filename,'r').read().strip().split('\n')[1:]
	p = 0
	for row in data:
		p+=1
		a = list(row)
		a = [int(x) for x in a]
		while not tidy(a):
			a = refine(a)
		print ''.join(['Case #',str(p),': ',''.join([str(x) for x in a])])

if __name__ == '__main__':
   main()
