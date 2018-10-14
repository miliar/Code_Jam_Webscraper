def is_palindrome(num):
	from math import ceil
	snum = str(num)
	return reduce(lambda x,y:x and y,[snum[i] == snum[-(i+1)] for i in xrange(0,int(ceil(len(snum)/2.0)))],True)
	
def find_palindromes(start,end):
	return [x for x in xrange(start,end+1) if is_palindrome(x)]
	
def find_fair_square(start,end):
	from math import sqrt,ceil
	beg = int(ceil(sqrt(start)))
	end = int(sqrt(end))
	return [x**2 for x in find_palindromes(beg,end) if is_palindrome(x**2)]
	
if __name__ == "__main__":
	trials = int(raw_input())
	file = open("./output.txt",'w')
	
	for x in xrange(0,trials):
		data = raw_input().split()
		start = int(data[0])
		end = int(data[1])
		num = len(find_fair_square(start,end))
		file.write("Case #%i: %i\n" % (x+1,num))
		
	file.close()
		
		