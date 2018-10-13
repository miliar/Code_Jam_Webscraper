#hfjimenez@utp.edu.co codejam2017
def ordenado(val):
	valk=str(val)
	lenk=len(valk)
	for i in range(lenk-1):
		if valk[i]<valk[i+1] or valk[i]==valk[i+1]:
			continue 
		else: 
			return False
	#print(valk)
	return True

def solve(n):
	i=0							#how many times you iterate
	tmpn=int(n)
	while True:
		if ordenado(tmpn):
			newval=tmpn
			break
		else :
			#print("antes: {}".format(tmpn))
			tmpn=tmpn-1
			#print("despues-1: {}".format(tmpn))
			continue 

	return newval

t = int(input())  
n=[]
for i in range(t):
	n.append(input())	
	print("Case #{}: {} ".format(i+1,solve(n[i])))