
	
file_in = 'B-large.in'
file_out = 'out.txt'
with open(file_in,'rb') as fin, open(file_out,'w') as fout:
	lines = fin.read().splitlines()
	case = 1
	for l in lines[1:]:
		# print (l)
		i = int(l.split()[0])
		while i > 0:
			_list = [int(x) for x in list(str(i))]
			_list_sorted = sorted(_list, key=int)
			str1 = ''.join([ str(x) for x in _list_sorted ])
			# print (str(i) + " " + str1 + " " +str(i - int(str1)))
			if str1 == str(i):
				break
			for x, y in zip(range(0,len(_list)-1), range(1,len(_list))):
				if _list[x]>_list[y]:
					_min_index = y
					break
			for x in range(_min_index, len(_list)):
				_list[x] = 0
			i = int(''.join([ str(x) for x in _list ]))
			i = i-1	

		output = 'Case #%d: %s\n' % (case,i)
		fout.write(output)
		case += 1


		