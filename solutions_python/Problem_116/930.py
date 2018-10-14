#coding: utf-8
#!/usr/bin/env python2.7
import sys
import copy

def solver(in_list, name):
	list = copy.copy(in_list)
#	print name
#	print list
	for l in range(4):
		for i in range(4):
			if list[l][i] == 'T': 
				list[l] = list[l][:i]+name+list[l][i+1:]
#	print list
	
	for l in list:
		flag = 1
		for i in range(4):
			if l[i] != name: flag = 0
		if flag: return 1	# won
	
	for i in range(4):
		flag = 1
		for j in range(4):
			if list[j][i] != name: flag = 0
		if flag: return 2
	
	if list[0][0] == list[1][1] == list[2][2] == list[3][3] == name: return 3
	if list[0][3] == list[1][2] == list[2][1] == list[3][0] == name: return 4
	
	return 0
	


def main():
	line = []
	for l in sys.stdin: line.append(l)

	counter = 0
	num = int(line[counter][:-1])
	counter += 1

	for i in range(1, num+1):
		line1 = line[counter][:-1]
		counter += 1
		line2 = line[counter][:-1]
		counter += 1
		line3 = line[counter][:-1]
		counter += 1
		line4 = line[counter][:-1]
		counter += 1
		counter += 1
		list = [line1, line2, line3, line4]
#		print 'ner line : ', list

		ans = solver(list, 'X')
		if ans:
			print 'Case #%s: %s won' % (str(i), 'X')
		else:
			ans = solver(list, 'O')
			if ans: print 'Case #%s: %s won' % (str(i), 'O')
			else:
				flag = 0
				for l in list:
					for j in range(4):
						if l[j] == '.': 
							print 'Case #%s: Game has not completed' % (str(i))
							flag = 1
							break
					if flag: break
				if flag == 0:  print 'Case #%s: Draw' % (str(i))

if __name__ == '__main__':
	main()
