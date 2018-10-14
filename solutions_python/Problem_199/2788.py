t = int(input())
#print(t)
import sys
sys.setrecursionlimit(10000)
def opcon(s):
	if s=="+":
		return 1
	return 0
def bitflip(ba,K,sp):
	for i in range(sp,sp+K):
		#print(i)
		ba[i]=(ba[i]+1)%2
	return ba
def minflips(target,cakes,K):
	#print(cakes)
	if len(cakes)<K:
		if sum(cakes)==target*len(cakes):
			return 0
		return 10000000000
	if sum(cakes[0:K])==K*target:
		return minflips(target, cakes[K:],K)
	if sum(cakes[-K:])==K*target:
		return minflips(target, cakes[0:-K],K)
	for sp in range(0,min(K,len(cakes)-K+1)):
		#print("d")
		#print(len(cakes)-K)
		#print(cakes)
		#print(sp)
		if cakes[sp]!=target:
			return minflips(target,bitflip(cakes,K,sp),K)+1
		#if cakes[-(sp+1)]!=target:
			#return minflips(target,bitflip(cakes,K,len(cakes)-sp-K),K)+1
	return 10000000000
for i in range(1, t + 1):
	pancakes,K=[s for s in input().split(" ")]
	K=int(K)
	nc=len(pancakes)
	cakes = [opcon(s) for s in pancakes]

	#print(K)
	#print(pancakes)
	#print(cakes)
	#print(nc)
	if sum(cakes)==nc:
		print("Case #{}: 0".format(i))
	else:
		cakes2=list(cakes)
		flips=minflips(1,cakes,K)
		if flips<10000000000:
			print("Case #{}: {}".format(i,flips))
		else:
			print("Case #{}: IMPOSSIBLE".format(i))
	#for i in range(0,)