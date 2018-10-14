#z=int(input())
#x=0
#while z < z:
def gt(j):
	s=input().split()
	c=float(s[0])
	f=float(s[1])
	x=float(s[2])
	r=2
	fn=0
	gt=0
	while True:
		ct=x/r
		ft=x/(r+f)
		ff=c/r
		if ff+ft<ct:
			gt=gt+ff
			r=r+f
		else:
			break
	gt=gt+ct
	print("Case #"+str(j)+": "+str(gt))
def main():
	d=int(input())
	j=0
	while j<d:
		gt(j+1)
		j=j+1
	return 0
if __name__ == '__main__':
	main()
