
def REK(pancakes,hashh):
	if tuple(pancakes) in hashh:
		return (hashh[tuple(pancakes)],hashh)
	if pancakes[-1]==1:
		hashh[tuple(pancakes)]=1
		return(1,hashh)
	ans=pancakes[-1]
	for ny in range(2,pancakes[-1]):
		(k,hashh)=REK(sorted([ny]+[pancakes[-1]-ny]+pancakes[:-1]),hashh)
		ans=min(1+k,ans)
	hashh[tuple(pancakes)]=ans
	return (ans,hashh)

f=open("B-small-attempt3.in","r")
g=open("OUTPUT.txt","w+")
T=int(f.readline())
for i in range(T):
	D=int(f.readline())
	pancakes=[int(j) for j in f.readline().split()]
	pancakes.sort()
	
	(ans,hashh)=REK(pancakes,{})
	print("Case #{}: {} {}\n".format(i+1,ans,pancakes))
	#klkl=input("NEXT: ")
	g.write("Case #{}: {}\n".format(i+1,ans))

f.close()
g.close()
