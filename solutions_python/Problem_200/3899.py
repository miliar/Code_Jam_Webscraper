t = int(input())
n = []
for i in range(1, t + 1):
	formated = input().split(" ")
	n.append(formated[0])

def isTidy(num):

	converted = list(str(num))
	first = converted[0]
	for element in converted[1:]:
		if first<=element:
			first = element

		else:
			return False


	return True


ans = []
for element in n:
	int_element = int(element)
	if(True):
		nines=[]
		i=len(element)
		rest= str(int_element)[:i+1]
		while(int(rest)>=0):
			if isTidy(int(rest)):
				if(str(rest)[0]=="0"):
					ans_large = str(rest)[1:]
				else:
					ans_large = str(rest)

				break

			else:
				i-=1
				rest= str(int_element)[:i]
				rest = int(rest)-1
				nines.append("9")
				
				
		
		ans_large +=''.join(nines)
		ans.append(int(ans_large))


for i in range(len(n)):
	res = [str(s) for s in ans]   # read a list of integers, 2 in this case
	print("Case #{}: {}".format(i+1, res[i]))
			