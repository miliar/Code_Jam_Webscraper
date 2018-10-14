import sys
sys.stdin.readline()
i = 0
s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = 'yhesocvxduiglbkrztnwjpfmaq'
m = str.maketrans(s1,s2)

while True:
	s = sys.stdin.readline()
	if s == '':
		break
	i = i + 1
	print("Case #{}: {}".format(i, s.strip().translate(m)))
