import math as m

def calc(start, stop):
	start = m.ceil(m.sqrt(start))
	stop = m.floor(m.sqrt(stop))
	tot=0
	for i in range(int(start), int(stop+1)):
		if is_palindrome(i) and is_palindrome(i**2):
			tot+=1
	return tot

def is_palindrome(num):
	return str(num) == str(num)[::-1]

f = open('out.txt','w')
for i in range(int(raw_input())):
	inp = raw_input().split(' ')
	f.write('Case #%d: %d\n'%(i+1,calc(int(inp[0]),int(inp[1]))))
f.close()