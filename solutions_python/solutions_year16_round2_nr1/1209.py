count=[0]*10

def func(inp):
	if 'Z' in inp:
		count[0]+=1
		inp.remove('Z')
		inp.remove('E')
		inp.remove('R')
		inp.remove('O')
	elif 'X' in inp:
		count[6]+=1
		inp.remove('S')
		inp.remove('I')
		inp.remove('X')
	elif 'S' in inp:
		count[7]+=1
		inp.remove('S')
		inp.remove('E')
		inp.remove('V')
		inp.remove('E')
		inp.remove('N')
	elif 'W' in inp:
		count[2]+=1
		inp.remove('T')
		inp.remove('W')
		inp.remove('O')
	elif 'V' in inp:
		count[5]+=1
		inp.remove('F')
		inp.remove('I')
		inp.remove('V')
		inp.remove('E')
	elif 'G' in inp:
		count[8]+=1
		inp.remove('E')
		inp.remove('I')
		inp.remove('G')
		inp.remove('H')
		inp.remove('T')
	elif 'F' in inp:
		count[4]+=1
		inp.remove('F')
		inp.remove('O')
		inp.remove('U')
		inp.remove('R')
	elif 'T' in inp:
		count[3]+=1
		inp.remove('T')
		inp.remove('H')
		inp.remove('R')
		inp.remove('E')
		inp.remove('E')
	elif 'O' in inp:
		count[1]+=1
		inp.remove('O')
		inp.remove('N')
		inp.remove('E')
	elif 'N' in inp:
		count[9]+=1
		inp.remove('N')
		inp.remove('I')
		inp.remove('N')
		inp.remove('E')
	return inp

t = int(raw_input())
case = 1
while t!=0 :
	count = [0]*10
	fin = []
	inp = list(raw_input())
	while(''.join(inp)!=''):
		func(inp)
	i=0
	print 'Case #'+str(case)+':',
	case+=1
	while i<10:
		fin += str(str(i)*count[i])
		i+=1
	print ''.join(fin)
	t-=1