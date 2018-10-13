import sys
#sys.stdin = open('stdin.txt','r')
#sys.stdout = open('stdout.txt','w')
t=int(input())
for u in range(t):
	ans = 0.0
	d,n = map(float,input().split())
	if(n==1):
		k,s=map(float,input().split())
		time = (d-k)/s
		ans = d/time
	else:
		k1,s1 = map(float,input().split())
		k2,s2 = map(float,input().split())
		if(k1<k2):
			temp1,temp2=k1,s1
			k1,s1=k2,s2
			k2,s2=temp1,temp2
		fb = 0
		if(s2<=s1):
			fb = 2
		else:
			x=(s1*(k1-k2))/((s2-s1))
			if(k1+x>=d):
				fb = 2
			else:
				fb = 1
		if(fb==2):
			time = (d-k2)/s2
			ans = d/time
		else:
			time = (d-k1)/s1
			ans = d/time
	ansstring = "%.6f" % ans
	print("Case #"+str(u+1)+": "+ansstring)


