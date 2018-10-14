from collections import *
c=[]
o=[]

def pair(x,y):
	for e in c:
		if((e[0]==x and e[1]==y) or (e[0]==y and e[1]==x)):	return e[2]
	return False
	
def opp(str,w):
	for e in str:
		if (((e+w) in o) or ((w+e) in o)):	return True
	return False
	
def main():
	global c,o
	inp = open('input', 'r')
	out = open('output', 'w')
	g = []
	n = -1
	for row in inp:
		n = n+1
		g = row.split()
		print g
		l = len(g)
		if(l>1):
			a = int(g[0])
			b = int(g[a+1])
			c = []
			o = []
			i = 0
			print a,b
			while(i<a):
				c.append(g[i+1])
				i = i+1
			i = 0
			while(i<b):
				o.append(g[a+2+i])
				i=i+1
			s = g[a+b+3]
			print s,g[a+b+3]
			ans = s[0]
			i = 1
			while(i<len(s)):
				if(ans):
					t1 = pair(ans[-1],s[i])
					t2 = opp(ans,s[i]) 
					if(t1):	ans = ans[0:-1] + t1
					elif(t2):	ans = ''
					else:	ans = ans + s[i]
				else:	ans = ans+s[i]
				i = i+1
			out.write('Case #')
			t = str(n)
			out.write(t)
			out.write(': [')
			i=0
			while(i<(len(ans)-1)):
				out.write(ans[i])
				out.write(', ')
				i = i+1
			if(ans):
				out.write(ans[-1])
			out.write(']\n')
		#print t
	return 0

if __name__ == '__main__':
	main()
