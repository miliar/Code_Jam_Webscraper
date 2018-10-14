f1 = open('A-1.in', 'r')
f2 = open('A-2.in', 'r')

mapping = [-1 for i in range(26)]

while (1):
	a = f1.read(1) 
	b = f2.read(1)
	if (a == ' ' or a == '\n'):
		continue
	if (a == ''):
		break
	mapping[ord(a) - 97] = ord(b) - 97	

mapping[ord('q') - 97] = ord('z') - 97
mapping[ord('z') - 97] = ord('q') - 97
#for i in range(26):
#	print chr(97 + i), chr(97 + mapping[i])

f1.close()
f2.close()

f1 = open('A.in', 'r')
f2 = open('A.out', 'w')

T = int(f1.readline())
t = 1
print >>f2, 'Case #%d: ' % t,


while (1):
	a = f1.read(1)
	if (a == ''):
		break
	if (a == ' '):
		f2.write(a)
		continue
	if (a == '\n'):
		t += 1
		if (t > T):
			break
		print >>f2, '\n', 'Case #%d: ' % t,
		continue	
	f2.write(chr(97 + mapping[ord(a) - 97]))


	
