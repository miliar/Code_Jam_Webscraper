
def findTidy(N) :
	ret = ""
	N = str(int(N))
	length = len(N) - 1
	ok = True
	while length > 0 :
		current = int(N[length])
		prec = int(N[length -1])
		if current > 0 :
			if not ok :
				current -= 1
				ok = True
		else:
			if not ok :
				current = 9 

		if(current >= prec) :
			ok = True
			ret = `current` + ret
		else:
			ok = False
			ret = '9' * (len(ret)+1)
		length -= 1

	current = int(N[length])
	if ok:
		ret = `current` + ret
	else :
		if current != 1:
			ret = `current-1` + ret
	return ret


with open("test.txt") as fd :

	content = fd.readlines()
	T = content[0]
	i = 1
	with open('result.txt', 'w') as fr:
		for case in content[1:] :
			fr.write("Case #" + `i` + ": " + findTidy(case)+"\n")
			i +=1
		