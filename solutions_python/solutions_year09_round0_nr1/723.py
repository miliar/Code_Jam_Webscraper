import sys
import re

words = []
datas = []

def main():
	
	fp = open('A-large.in', 'r')
	
	args = fp.readline()
	args = args.split(' ')
	L = int(args[0])
	D = int(args[1])
	N = int(args[2])
	
	for i in range(D):
		word = fp.readline()
		words.append(word)
	
	for i in range(N):
		data = fp.readline()
		data = data.replace('(', '[').replace(')', ']')
		datas.append(data)
		
def output():
	fp1 = open('A-large.out.txt', 'w')
	
	for data in datas:
		pattern = data
		count = 0
		
		for word in words:
			if re.search(data, word):
				count = count + 1
		fp1.write ( "Case #%s: %s\n" % (datas.index(data)+1, count))
	
	
if __name__ == '__main__':
	main()
	output()