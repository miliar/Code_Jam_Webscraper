'''
Created on Sep 13, 2009
@author: namnx
'''

INFILE = 'prob1-large.in'
OUTFILE = 'prob1-large.out'


def findOrder(s):
	order = []
	order.append('')
	order.append(s[0])
	if len(s) < 2:
		return order
	pos0 = 1
	while (pos0 < len(s) and s[pos0] == s[0]): pos0 +=1
	if pos0 == len(s):
		return order
	order[0] = s[pos0]
	for i in range(pos0+1, len(s)):
		if order.count(s[i]) == 0:
			order.append(s[i])
	return order


def convertToDecimal(list, base):
	val = 0
	k = 1
	for i in range(0,len(list)):
		val += k * list[len(list)-1-i]
		k *= base
	return val
 
	
def findValue(s):
	order = findOrder(s)
	base= len(order)
	l = []
	for c in s:
		l.append(order.index(c))
	return convertToDecimal(l, base) 



def main():
	fin = file(INFILE, 'r')
	fout = file(OUTFILE,'w')
	t = int(fin.readline())
	for i in range(t):
		line = fin.readline().strip()
		val = findValue(line)
		fout.write('Case #' + str(i+1) + ': ' + str(val) + '\n')
	fin.close()
	fout.close()
	
	
if __name__ == '__main__':
	main()
	
	