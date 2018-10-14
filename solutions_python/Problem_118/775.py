import networkx as nx
from random import randint
import sys
from countutil import *
from bisect import bisect
import itertools

		
def reverse(sequence):
	rev = []
	for i in range(len(sequence)-1,-1,-1):
		rev.append(sequence[i])
	return rev

def sub_iterator(repeat):
	for sequence in itertools.product(['0','1','2'],repeat=repeat):
		rev = reverse(sequence)
		seq = ''.join(list(sequence) + rev[1:])
		num =  long('1'+seq+'1')
		num2 = long('2'+seq+'2')	
		yield long(math.pow(num,2))
		yield long(math.pow(num2,2))
		seq2 = ''.join(list(sequence) + rev)
		num =  long('1'+seq2+'1')
		num2 = long('2'+seq2+'2')	
		yield long(math.pow(num,2))
		yield long(math.pow(num2,2))		
		
		
def iterators():
	allnums = []
	for repeat in range(1,10):
		for element in sub_iterator(repeat):
			yield element
	
				
def train():
	allnums = [1,4,9,121,484]
	limit = long(math.pow(10,100))
	for num in iterators():
		if palindrome(num):
			print 'solution',long(math.sqrt(num)),num
			allnums.append(num)
	pickle.dump(sorted(allnums),open("source/allnums.pkl","w"))
	return allnums
	
def palindrome(number):
	number=str(number)
	for i in range(len(number)):
		if number[i]!=number[-1-i]:
			return False
	return True

def fair_up_to(num,allnums):
	return bisect(allnums,num)
	
def make_decision(low,high):
	try:
		allnums = pickle.load(open("source/allnums.pkl",'r'))
	except:
		allnums = train()
	return str(long(fair_up_to(high,allnums)-fair_up_to(low-1,allnums)))
	
def read_input(size):
	problem='C'
	reader = get_reader(problem,size)
	writer = get_writer(problem,size)
	cases= reader.next()
	for case in range(int(cases)):
		low,high = reader.next().strip().split()
		decision = make_decision(long(low),long(high))
		writer.write( "Case #"+str(case+1)+": "+decision+'\n')
	increment_count(problem,size)
	writer.close()
		
if __name__=='__main__':
	size = sys.argv[1]
	read_input(size)