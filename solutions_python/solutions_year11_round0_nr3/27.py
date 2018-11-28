
def main():
	fin = open('C-large.in','r')
	fout = open('output.txt','w')
	
	T = int(fin.readline())
	
	for i in range(T):
		fin.readline()
		candies = map(int,fin.readline().strip().split(' '))
		candies.sort()
		
		if reduce(lambda x,y:x^y,candies) == 0:
			print 'Case #' + str(i+1) + ': ' + str(sum(candies) - candies[0])
			fout.write('Case #' + str(i+1) + ': ' + str(sum(candies) - candies[0]) + '\n')
		else:
			print 'Case #' + str(i+1) + ': NO'
			fout.write('Case #' + str(i+1) + ': NO\n')	

if __name__ == '__main__':
	main()
