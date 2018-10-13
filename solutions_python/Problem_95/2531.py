import math

def main():
	d = { 'a' : 'y', 'b' : 'h','c' : 'e','d' : 's','e' : 'o','f' :	'c','g' : 'v','h'	: 'x','i' :	'd','j' : 'u','k' : 'i','l' : 'g','m' : 'l' \
         ,'n' : 'b', 'o' : 'k','p' : 'r','q' : 'z','r' : 't','s' : 'n','t' : 'w','u' : 'j','v' :	'p','w' : 'f','x' : 'm','y' : 'a','z' : 'q', ' ' : ' ', '\n' : '\n'}
	L = []
	g = open('/home/varun/Desktop/Programs/A-small-attempt3.in','r')
	f = open('/home/varun/Desktop/Programs/out.txt','w')
	for line in g:
		L.append(line)
	n = int(L[0]) 
	c = 0
	while c < n:
		strin = L[c+1]
		s = ''
		for i in strin:
			s = s+d[i]
		f.write("Case #%d: %s"%((c+1),s))
		c = c + 1
	f.close()

if __name__=="__main__":
	main()
