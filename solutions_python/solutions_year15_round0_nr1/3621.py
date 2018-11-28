text = open('test.in','r')
output = open('out.txt','r+')

def solve(max, audience):
	i = 2
	answer = 0
	people = 0
	while(i <= (max + 2)):
		
		if((answer + people) < (i - 2)):
			answer += 1
		elif(i != (max + 2)):
			people += int(audience[i])
			i += 1			
		else:
			i += 1
	return answer

count = 0
ans = 0			
Tests = int(text.readline())
while count < Tests:
	input = text.readline()
	Smax = int(input[0])
	ans = solve(Smax, input)
	count += 1
	print "Case #%s: %d" %(count, ans)
	output.write("Case #%s: %d\n" %(count, ans))
text.close()
output.close()