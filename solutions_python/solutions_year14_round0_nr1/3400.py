def t(ca):
	r1=int(input())
	c=1
	while c<r1:
	   t=input()
	   c=c+1
	s1=input()
	s1=s1.split()
	while c<4:
	   t=input()
	   c=c+1
	r2=int(input())
	z=1
	while z<r2:
	   t=input()
	   z=z+1
	s2=input()
	s2=s2.split()
	while z<4:
	   t=input()
	   z=z+1
	a=0
	for x in s1:
	   if x==' ':
	      continue
	   try:
	      r=s2.index(x)
	      a=a+1
	   except ValueError:
	      e=1
	ca=str(ca+1)
	if a>1:
		print("Case #"+ca+": Bad magician!")
	elif a==0:
		print("Case #"+ca+": Volunteer cheated!")
	else:
		print("Case #"+ca+": "+str(s2[r]))
	return 0


def main():
	d=int(input())
	j=0
	while j<d:
		t(j)
		j=j+1
	return 0

if __name__ == '__main__':
	main()

