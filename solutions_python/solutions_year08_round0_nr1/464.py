def ans(answer, case):
	global out
	case = str(case+1)
	answer = str(answer)
	out.write("Case #"+case+": "+ answer+"\n")
def stuff(querries, engines, case):
	changes = 0
	while len(querries):
		for i in engines:
			if i not in querries:
				ans(changes, case)
				return
		high = 0
		try:
			lastEngine = nextEngine
		except:
			lastEngine = None
		nextEngine = None
		nextPrev = None
		high2 = None
		highs = []
		for i in engines:
			if high < querries.index(i):
				high = querries.index(i)
				#prevEngine = nextEngine
				nextEngine = i

			if high2 < querries.index(i):
				high2 = querries.index(i)
				highs.append(high2)
		high2 = highs[len(highs)-2]
		if nextEngine is lastEngine:
			nextEngine = querries[high2]

		changes += 1
		for i in range(0,high):
			querries.pop(0)
	ans(changes, case)
def main():
	info = open("file").read()
	info = info.split("\n")
	pos = 0
	
	cases = int(info[pos])
	for case in range(cases):
		pos += 1
		engineNum = int(info[pos])
		engines = []
		for i in range(engineNum):
			pos += 1
			engines.append(info[pos])
		pos+=1
		querryNum = int(info[pos])
		querries = []
		for i in range(querryNum):
			pos += 1
			querries.append(info[pos])
		stuff(querries, engines, case)
out = open("out", "w")
main()