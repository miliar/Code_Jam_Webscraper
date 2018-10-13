tests=int(raw_input())
info=[]
for x in range (0,tests):
	a=raw_input()
	info.append(a)
for o in range (0,tests):
	case=info[o]
	max=int(case[0])
	data=case[2:]
	state=0
	need=0
	ppl=0
	for x in data:
		x=int(x)
		if x>0 and state>ppl:
			add=state-ppl
			need+=add
			ppl+=add
		ppl+=x
		state+=1	
	res = "Case #" + str(o+1) + ": " + str(need)
	print res;;