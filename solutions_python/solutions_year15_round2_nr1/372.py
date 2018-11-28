import math

input_file = open('A-small-attempt8.in.txt')
output_file = open('output.txt', 'w')

Nsize = 1000001
dp = [0]*Nsize

def reverseNum(number):
	digits = []
	while (number):
		digits.append(number%10)
		number /= 10

	ans = 0
	while (digits):
		ans = ans*10 + digits.pop(0)
	return ans


#init
dp[1] = 1
for i in range(2,Nsize):
	dp[i] = Nsize+10
#table filling
for i in range(1,Nsize):
	if dp[i]>dp[i-1]+1:
		dp[i] = dp[i-1]+1
	rv = reverseNum(i)
	if dp[rv]>dp[i]+1:
		dp[rv] = dp[i]+1


input_file.readline()
linecnt = 1;
for line in input_file:
	answer = dp[int(line)]
	outputstring = "Case #%s: %s\n"%(linecnt, answer)
	output_file.write(outputstring)
	linecnt+=1

input_file.close()
output_file.close()

print reverseNum(51)
print reverseNum(2134101123)
print reverseNum(21341)
print reverseNum(1010101)
print reverseNum(1004)
print reverseNum(2300)
print reverseNum(10)
