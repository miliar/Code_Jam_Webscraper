#!/bin/python
import sys

pat = {'i':{'r':{'in':'j','out':'k'}, 'l':{'in':'k', 'out':'-j'}}, 'j':{'r':{'in':'k','out':'i'}, 'l':{'in':'i', 'out':'-k'}}, 'k':{'r':{'in':'i','out':'j'}, 'l':{'in':'j', 'out':'-i'}}}
search = ['i','j','k']

def solve_it(string, j):
	if '-' not in string[j] and j < len(string)-1:
		if string[j+1] == pat[string[j]]['r']['in']:
			string[j+1] = pat[string[j]]['r']['out']
		elif string[j+1] == pat[string[j]]['l']['in']:
			string[j+1] = pat[string[j]]['l']['out']
		else:
			if (j+1)< len(string)-1:
				j += 1
			else:
				string[j+1] = '-1'
				return (j+1)
			string[j+1] = '-'+string[j+1]

	elif j < len(string)-1:
		newStr = list(string[j])[1]
		if string[j+1] == pat[newStr]['r']['in']:
			string[j+1] = '-'+pat[newStr]['r']['out']
		elif string[j+1] == pat[newStr]['l']['in']:
			string[j+1] = list(pat[newStr]['l']['out'])[1]
		else:
			if (j+1)< len(string)-1:
				j += 1
			else:
				string[j+1] = '1'
				return (j+1)

	# print("After: ", string)
	# print("Count: ", count)
	# print("------------------------\n")
	return (j+1)

if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	count=0
	test = int(f.readline())
	for i in range(test):
		letters, times = f.readline().split()
		letters = int(letters)
		times = int(times)
		j=1
		letterSet = f.readline().rstrip("\n")
		if(letters == 1):
			print('Case #%d: NO'%(i+1))
			continue

		string = list(letterSet)
		while(j<times):
			string.extend(list(letterSet))
			j += 1
		j=0
		count=0
		while(j<len(string)):
			if string[j] == search[count]:
				count += 1
				j += 1
				if(count<3):
					continue
				else:
					string[j-1] = '1'
					break

			j=solve_it(string, j)

		while(j<len(string)):
			j=solve_it(string, j)
			

		if count > 2 and string[j-1] == '1':
			print('Case #%d: YES'%(i+1))
		else:
			print('Case #%d: NO'%(i+1))

