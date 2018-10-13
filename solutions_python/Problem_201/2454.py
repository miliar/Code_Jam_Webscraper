
def getTestCases():
	num = int(raw_input())
	n = []
	k = []
	for i in range(0,num):
		nt, nk = map(int,raw_input().split())
		n.append(nt)
		k.append(nk)
	return num,n,k

def getLandR(stalls, i):
	L = 0
	R = 0
	for x in range(i+1,len(stalls)-1):
		if stalls[x] == 0:
			R += 1
		else:
			break
	#print( range(i-1,0,-1))
	for y in range(i-1,0,-1):
		if stalls[y] == 0:
			L += 1
		else:
			break
	#print (L)
	#print (R)
	#print()
	return L,R

def getLSandRS(stalls):
	ls_l = []
	rs_l = []
	stall_i = []
	for i in range(0,len(stalls)):
		if stalls[i] == 0:
			l, r = getLandR(stalls,i)
			ls_l.append(l)
			rs_l.append(r)
			stall_i.append(i)
	return stall_i,ls_l,rs_l

def chooseStall(stalls):
	stall_i,ls_l,rs_l = getLSandRS(stalls)

	max_ls_rs = -1
	max_i = -1
	collisions = []
	for i in range(0,len(stall_i)):
		m = min(ls_l[i],rs_l[i])
		if (m > max_ls_rs):
			max_ls_rs = m
			max_i = stall_i[i]
			collisions[:] = []
			collisions.append([ls_l[i], rs_l[i], max_i])
		if (m == max_ls_rs):
			collisions.append([ls_l[i], rs_l[i], stall_i[i]])

	#only one possible min(ls,rs) 
	if len(collisions) == 1:
		if stalls[collisions[0][2]] == 1:
			print ("wtf")
			print (stalls)
		stalls[collisions[0][2]] == 1
		return stalls

	min_ls_rs = -1
	min_i = -1
	new_collisions = []
	for i in range(0,len(collisions)):
		ls, rs, ind = collisions[i][0], collisions[i][1], collisions[i][2]
		m = max(ls,rs)
		if (m > min_ls_rs):
			min_ls_rs = m
			min_i = ind
			new_collisions[:] = []
			new_collisions.append([ls, rs, ind])
		if (m == min_ls_rs):
			new_collisions.append([ls, rs, ind])

	if stalls[new_collisions[0][2]] == 1:
		print ("wtf2")
		print (stalls)
	stalls[new_collisions[0][2]] += 1
	return stalls,new_collisions[0][0],new_collisions[0][1]

def placePeopleInStalls(stalls, k):
	for i in range(0,k):
		stalls,l,r = chooseStall(stalls)

	return l,r

def min(num1, num2):
	if (num1 > num2):
		return num2
	return num1

def max(num1, num2):
	if num1 > num2:
		return num1
	return num2

if __name__ == '__main__':
	num,n,k = getTestCases()
	print(num)
	for i in range(0,num):
		N = n[i]
		P = k[i]
		stalls = [1]
		for x in range(0,N):
			stalls.append(0)
		stalls.append(1)

		mn, mx = placePeopleInStalls(stalls,P)
		print('Case #'+str(i+1)+': ' + str(mx) +' '+ str(mn))


