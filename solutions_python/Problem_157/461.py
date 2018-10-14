quat_map = {
	'1':{
		'1':'1',
		'i':'i',
		'j':'j',
		'k':'k',
		'-1':'-1',
		'-i':'-i',
		'-j':'-j',
		'-k':'-k'
	},
	'i':{
		'1':'i',
		'i':'-1',
		'j':'k',
		'k':'-j',
		'-1':'-i',
		'-i':'1',
		'-j':'-k',
		'-k':'j'
	},
	'j':{
		'1':'j',
		'i':'-k',
		'j':'-1',
		'k':'i',
		'-1':'-j',
		'-i':'k',
		'-j':'1',
		'-k':'-i'
	},
	'k':{
		'1':'k',
		'i':'j',
		'j':'-i',
		'k':'-1',
		'-1':'-k',
		'-i':'-j',
		'-j':'i',
		'-k':'1'
	},
	'-1':{
		'-1':'1',
		'-i':'i',
		'-j':'j',
		'-k':'k',
		'1':'-1',
		'i':'-i',
		'j':'-j',
		'k':'-k'
	},
	'-i':{
		'-1':'i',
		'-i':'-1',
		'-j':'k',
		'-k':'-j',
		'1':'-i',
		'i':'1',
		'j':'-k',
		'k':'j'
	},
	'-j':{
		'-1':'j',
		'-i':'-k',
		'-j':'-1',
		'-k':'i',
		'1':'-j',
		'i':'k',
		'j':'1',
		'k':'-i'
	},
	'-k':{
		'-1':'k',
		'-i':'j',
		'-j':'-i',
		'-k':'-1',
		'1':'-k',
		'i':'-j',
		'j':'i',
		'k':'1'
	}
}
def mult(a,b):
	return quat_map[a][b]

def check_quat(letters):
	first = '1'
	for i in range(len(letters)-2):
		first = mult(first,letters[i])
		if first == 'i':
			second = '1'
			for j in range(i+ 1, len(letters) - 1):
				second = mult(second,letters[j])
				if second == 'j':
					third = '1'
					for k in range(j+1,len(letters)):
						third = mult(third,letters[k])
					if third == 'k':
						return True
					break
			break
	return False

with open('C-small-attempt1.in') as f:
	with open('C-small-attempt1.out','w') as of:
		t = int(f.readline())
		for case_num in range(t):
			[l,x] = f.readline().split(" ")
			letters = f.readline()[0:int(l)] * int(x)
			if check_quat(letters):
				of.write("Case #{}: YES\n".format(case_num + 1))
			else:
				of.write("Case #{}: NO\n".format(case_num + 1))