def chkpos(s,p):
	if s[p] == "1":
		return False
	else:
		return True

def walkin(s):
	o = []
	for i in range(0, len(s)):
		if chkpos(s, i) == True:
			if i != 0:
				if i != len(s)-1:
					j = i
					f = i
					ls = 0
					rs = 0
					while(chkpos(s,j-1)):
						ls+=1
						j-=1
					while(chkpos(s,f+1)):
						rs+=1
						f+=1
					mn = min(ls,rs)
					mx = max(ls,rs)
					o.append([mn,mx,i])
					#print(o)
	return o
def decide(o):
	selected = [0,0,0];
	for i in range(0,len(o)):
		if o[i][0] > selected[0]:
			selected = o[i]
		elif o[i][0] == selected[0]:
			if o[i][1] > selected[1]:
				selected = o[i]
	#print("options", o)		
	#print("selected", selected)
	return selected

def solve(n,k):
	s = "1"
	for i in range(0,n):
		s+="0"
	s+="1"
	s = list(s)
	#print(s)
	for i in range(0, k):
		o = walkin(s)
		selected = decide(o)
		s[selected[2]] = "1"
		#print(i,s)
	result = str(selected[1])+ " " + str(selected[0])
	return result
	
t=int(input())
for cas in range(1,t+1):
	row = input()
	row = row.split(" ")
	n = int(row[0])
	k = int(row[1])
	print ("Case #{}: {}".format(cas,solve(n,k)))

	