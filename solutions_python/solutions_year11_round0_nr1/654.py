from collections import *

def main():
	inp = open('input', 'r')
	out = open('output', 'w')
	g = []
	n = -1
	for row in inp:
		n = n+1
		g = row.split()
		l = len(g)
		#print g,l
		k = 1
		i = 1
		j = 1
		t = 0
		a = deque([])
		b = deque([])
		if (l>1):
			x = g[k]
			flag = x
			if(k<l):
				while(g[k]==x):
					a.append(int(g[k+1]))
					k = k+2
					if(k>=l):	break
			
			if(k<l):
				y = g[k]
				while(g[k]==y):
					b.append(int(g[k+1]))
					k=k+2
					if(k>=l):	break
			while(1):
				f = 0
				if(len(a)):		
					if(a[0]>i):
						i = i + 1
					elif(a[0]<i):
						i = i-1
					elif(a[0]==i and flag==x):
						f = 1
						a.popleft()
						if(len(a)==0):
							flag = y
							if(k<l):
								while(g[k]==x):
									a.append(int(g[k+1]))
									k = k+2
									if(k>=l):	break
				if(len(b)):
					if(b[0]>j):
						j = j + 1
					elif(b[0]<j):
						j = j-1
					elif(b[0]==j and flag==y and f==0):
						b.popleft()
						if(len(b)==0):
							flag = x
							if(k<l):
								while(g[k]==y):
									b.append(int(g[k+1]))
									k = k+2
									if(k>=l):	break
				t = t+1
				if(len(a)==0 and len(b)==0):	break
				#print t, k, len(a), len(b), a, b, i, j				
		if(t):
			out.write('Case #')
			s = str(n)
			out.write(s)
			out.write(': ')
			s = str(t)
			out.write(s)
			out.write('\n')
		#print t
	return 0

if __name__ == '__main__':
	main()
