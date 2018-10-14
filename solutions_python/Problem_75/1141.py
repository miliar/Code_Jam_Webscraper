import sys

def self():
	time_taken_O = 0;
	time_taken_B = 0;
	position_O = 1;
	position_B = 1;
	time = 0
	push = 1

	filename = 'test.in'
	if len(sys.argv)==2:
		filename = sys.argv[1]
	out = filename[:-3]+'.out'
	print out
	f = open(filename)
	w = open(out, 'w')
	tests = int(f.readline())
	elements = ('Q','W','E','R','A','S','D','F')

	i = 0
	while i < tests:
		combine = dict()
		oppose = dict()
		print i
		i = i+1
		line = f.readline()
		pieces = line.split(' ')
		print pieces
		merges = int(pieces[0])
		
		iter = 0
		while iter < merges:
			iter = iter +1
			merge = pieces[iter]
			combine[merge[:2]] = merge[-1:]
		iter = iter +1
		
		clashes = int(pieces[iter])
		print 'iter = ',iter
		while iter < clashes+merges+1:
			iter = iter +1
			clash = pieces[iter]
			if clash[0] in oppose:
				oppose[clash[0]] = oppose[clash[0]].append(clash[1])
			else:
				oppose[clash[0]] = list(clash[1])
				
			if clash[1] in oppose:
				oppose[clash[1]] = oppose[clash[1]].append(clash[0])
			else:
				oppose[clash[1]] = list(clash[0])
			
		iter = iter+1
		
		length = int(pieces[iter])
		elements = pieces[iter+1]
		mylist = list()
		iter = 0
		print 'combine = ',combine
		while iter < length:
			if len(mylist) ==0:
				mylist.append(elements[iter])
			else:
				next = elements[iter]
				prev = mylist.pop()
				if next+prev in combine:
					mylist.append(combine[next+prev])
					next = combine[next+prev]
				elif prev+next in combine:
					mylist.append(combine[prev+next])
					next = combine[prev+next]
				else:
					mylist.append(prev)
					mylist.append(next)
				if next in oppose:
					for element in oppose[next]:
						if element in mylist:
							mylist = list()
			print mylist
			iter = iter+1
			
		if len(mylist) == 0:
			w.write('Case #'+str(i)+': [')
		else:
			w.write('Case #'+str(i)+': ['+mylist[0])
			j = 1
			while j < len(mylist):
				w.write(', '+mylist[j])
				j = j+1
		w.write(']\n')


if __name__ == "__main__":
	self()
