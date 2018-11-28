table={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
f=open('in','r')
w=open('out','w')
case=1
f.readline()

for line in f.readlines():
	s=''
	for c in line:
		if c=='\n':
			break;
		s+=table[c]
	w.write('Case #'+str(case)+': '+s+'\n')
	case+=1

f.close()
w.close()
