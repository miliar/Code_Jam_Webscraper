import re

# get list of palindrome squares from http://www.fengyuan.com/palindrome.html
# regex the html for numbers
# filter anything that isn't a palindrome square of a palindrome
# return a sorted list of fair and square numbers
def data_get():
	f = open('palin.txt','r')
	l = f.read()
	f.close()
	reg = re.findall("[0-9]+",l)
	palins = []
	for i in reg:
		k = int(i)
		if isPalin(k):
			if isPalin(int(k**0.5)) and (int(k**0.5) == k**0.5):
				palins.append(int(i))
	palins = list(set(palins))
	palins.sort()
	for i in palins:
		if isPalin(int(i**2)) and int(i**2) not in palins:
			palins.append(int(i**2))
	palins.sort()
	return palins
	
def solver(a,b,p):
	start = 0
	end = len(p)-1
	while p[start] < a:
		start += 1
	while p[end] > b:
		end -= 1
	return end-start+1
	
def input(filename):
	f = open(filename,'r')
	l = f.readlines()
	f.close()
	for i in range(len(l)-1):
		l[i] = l[i][:-1]
	p = data_get()
	f = open(filename + ' output','w')
	for i in range(int(l[0])):
		k = l[i+1].split(' ')
		a = int(k[0])
		b = int(k[1])
		s = 'Case #' + str(i+1) + ': ' + str(solver(a,b,p))+'\n'
		f.write(s)
	f.close()
	
def isPalin(i):
	s = str(i)
	for j in range(len(s)):
			if s[j] != s[len(s)-1-j]:
				return False
	return True