def getResult(num):
	digits = []
	for i in num:
		digits += [i]
	sorted = digits[:]
	sorted.sort()
	sorted.reverse()
	if sorted == digits:
		return ""
	bla = ""
	sorted.reverse()
	for i in sorted:
		if i > digits[0]:
			bla += i
			sorted.remove(i)
			break
	for i in sorted:
		bla += i
	return bla
	
		
	


def getRes(num):
	if len(num) == 1:
		return num + '0'
	answer = 1
	place = -2
	while(answer):
		#print num[place:]
		res = getResult(num[place:])
		if res != "":
			answer = 0
			return num[:place] + res
		place = place -1
		if (place * -1) > len(num):
			digits = []
			for i in num:
				digits += [i]
			digits.sort()
			digits = ['0'] + digits
			for i in range(0,len(digits)):
				if digits[i] != '0':
					resu = ""
					bla = [digits[i]] + digits[:i] + digits[i+1:]
					for i in bla:
						resu += i
					return resu

	
	
	
	
#print getResult("561")
#print getRes("982561")
	
file = open("c:\input.txt")
params = int(file.readline().strip())
for i in range(1, params+1):
	ans = getRes(file.readline().strip())
	print "Case #%s: %s" %(i,ans)