import sys

t = int(input())
for i in range (1,t+1):
	inp = str(input())
	j = 0 
	k = 1 #smallest
	if (len(inp)>1):
		while inp[j]<=inp[k] and k<len(inp):
			if inp[k-1]==inp[k]:
				k = k+1
			elif inp[k-1]<inp[k]:
				j = k
				k = k+1
			else:
				break
			if (k>=len(inp)):
				break
		if k<len(inp):
			inp = list(inp)
			inp[j] = str(int(inp[j])-1)
			for h in range(j+1,len(inp)):
				inp[h]='9'
			while(inp[0]=='0'):
				inp.pop(0)
			inp = ''.join(inp)
	print("Case #"+str(i)+": "+inp,end='\n')