import math

def getr(r):
    fst, snd = 0, 0
    for i in r:
        if i > fst:
            fst, snd = i, fst
        elif fst >= i > snd:
            snd = i
    return fst, snd
    
def rm(rh):
	fst,snd = getr(list(map(lambda rh: rh[0], rh)))
	cut = list(map(lambda rh: 2*rh[0]*rh[1] + (fst**2 - snd**2 if rh[0] == fst else 0), rh))
	rh.pop(cut.index(min(cut)))
	return rh
	
def calc():
	a, b = map(int, input().split())
	rh = []
	
	for i in range(a):
		c,d = map(int, input().split())
		rh.append((c,d))
		
	for i in range(a-b):
		rh = rm(rh)
		
	r = max(list(map(lambda rh: rh[0], rh)))
	c = sum(list(map(lambda rh: 2*rh[0]*rh[1], rh)))
	
	return (r*r+c)*math.pi
	
def main():
	c = int(input())
	
	for i in range(c):
		print("Case #"+str(i+1)+": "+str(calc()))

		
main()