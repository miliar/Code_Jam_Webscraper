s = [item.rstrip('\n') for item in open('text.txt','r').readlines()]

def toList(l):
	re = []
	for t in range(0, len(l)):
		for x in range(0,int(l[t])):
			re.append(t)
	return re
	
	
def main(si):
	p = 0
	st = []
	print si
	for t in si:
		if t > len(st):
			for a in range(0, t - len(st)):
				p +=1
				st.append(0)
		st.append(t)
		print st
		print t
	return p
	



text_file = open('Qout.txt', 'w')
for t in range(1, int(s[0])+1):
	text_file.write("Case #" + str(t) + ": " + str(main((toList(s[t][2::])))) + '\n')
text_file.close()