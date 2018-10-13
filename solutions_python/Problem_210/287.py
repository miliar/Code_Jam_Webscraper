t = int(input())
for test in range(t):
	ac,aj = [int(a) for a in input().split()]
	time = [' ']*1440
	for c in range(ac):
		ci,di = [int(a) for a in input().split()]
		for k in range(ci,di):
			time[k] = 'C'
	for j in range(aj):
		ci,di = [int(a) for a in input().split()]
		for k in range(ci,di):
			time[k] = 'J'

	smartSplit = False

	for st in range(0,720):
		onehalf = time[st:(st+720)]
		otherhalf = time[0:st] + time[(st+720):1440]
		one_elements = [x for x in list(set(onehalf)) if x != ' ']
		other_elements = [x for x in list(set(otherhalf)) if x != ' ']
		if(len(one_elements) <= 1 and len(other_elements) <= 1):
			if(len(one_elements) == 1 and len(other_elements) == 1):
				if (one_elements[0] == other_elements[0]):
					continue
			smartSplit = True
			break

	if smartSplit:
		print("Case #{}: {}".format(test+1,2))
	else:
		print("Case #{}: {}".format(test+1,4))
