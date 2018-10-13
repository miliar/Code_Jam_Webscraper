# your code goes here
test = input()
for i in range(1,int(test)+1):
	ans1 = int(input())
	l1=input().split()
	l2=input().split()
	l3=input().split()
	l4=input().split()
	ans2 = int(input())
	m1=input().split()
	m2=input().split()
	m3=input().split()
	m4=input().split()
	lc=[l1,l2,l3,l4]
	mc=[m1,m2,m3,m4]
	a1=lc[ans1-1]
	a2=mc[ans2-1]
	com=list(set(a1).intersection(set(a2)))
	if len(com)==0 :
		print("Case #"+str(i)+": Volunteer cheated!")
	elif len(com) > 1:
		print("Case #"+str(i)+": Bad magician!")
	else:
		print("Case #"+str(i)+": "+com[0])