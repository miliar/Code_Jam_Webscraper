
#returns list of indexes with occurrences of control in text
def Counter(control, text):
	#base: control is a char
	loo = []
	if len(control) == 1:
		for i in range(len(text)):
			if text[i] == control:
				loo.append(i)
		return loo
	
	#Hypothesis + step
	else:
		aux = Counter(control[1:], text)
		for i in aux:
			for j in range(len(text[:i])):
				if text[j] == control[0]:
					loo.append(j)
		return loo

def main():
	n = int(raw_input())
	control = "welcome to code jam"
	
	#n tests
	for i in range(1,n+1):
		count = 1
		text = raw_input()
		
		#sweeps text searching for matches
		num = str(len(Counter(control, text)))
		#output format
		if len(num) < 4:
			num = "0"*(4-len(num)) + num
		print "Case #" + str(i) + ": " + str(num[-4:])

if __name__ == "__main__":
    main()