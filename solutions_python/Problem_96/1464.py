import math

f = open("B-large.in","r") #"B-small-attempt0.in"
T = int(f.readline())

ret=""

for lineN in range(T):
	line = f.readline()
	line = line.split(" ")
	N=int(line[0])
	S=int(line[1])
	p=int(line[2])
	impossible=0
	mustBeSurprised=0
	done=0
	for i in range(3,3+N):
		t=int(line[i])
		if math.ceil(t/3)+1<p:
			impossible+=1
		elif math.ceil(t/3)>=p:
			done+=1
		else:
			if t>1 and t%3!=1:
				mustBeSurprised+=1
			else:
				impossible+=1
	ret+="Case #"+str(lineN+1)+": "+str(done+min(S,mustBeSurprised))+"\n"
f.close()
print(ret)
f=open("out.txt","w")
f.write(ret)