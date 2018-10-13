def Tidy(N):
	if N >= 0 and N <= 9:
		result = N
	else:
		digits = [int(char) for char in str(N)]
		len_N = len(digits)

		for i in list(reversed(range(1,len_N,1))):
			if digits[i] < digits [i-1]:
				# first conver all digits after i-1 to be 9
				for k in range(i,len_N,1):
					digits[k] = 9
				digits[i-1] = digits[i-1] - 1
		
		result = ConvInt(digits)	
	return result

def ConvInt(digits):
	total = 0
	rev_array = list(reversed(digits))
	for i in range(len(rev_array)):
		total = total + rev_array[i]*10**i
	return total

raw = []
with open("B-large.in") as f:
	for line in f:
		raw.append(int(line.strip('/n')))

T = raw.pop(0)
input_array = raw

for i in range(T):
	N = input_array[i]
	result = Tidy(N)
	print("Case #"+str(i+1)+":",result)


