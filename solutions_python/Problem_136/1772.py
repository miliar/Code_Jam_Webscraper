rate = 2.0

file_input = open('CookieClickerAlpha_input')
file_output = open('CookieClickerAlpha_output', 'w')

input = file_input.readline
print = file_output.write

T = int(input())

# Rate as a function of i farms
def R(F, i):
	return F*i + rate

# Time needed to aquire the ith farm
def t(C, F, i):
	return C/R(F, i - 1) # Rate when we own i - 1 farms

# Time taken to reach X based on number of farms we buy
def total_time(C, F, X, n):
	time = 0.0
	for i in range(1, n + 1):
		time += t(C, F, i)
	return time + X/R(F, n) # Rate after aquiring i farms = R(i)

for i in range(T):
	C, F, X = list(map(float, input().split()))
	nFarms = 0
	lastTime = float('inf') # Infinite time
	while(True):
		time = total_time(C, F, X, nFarms)
		if time > lastTime:
			break
		nFarms += 1
		lastTime = time
	print('Case #' + str(i + 1) + ': ' + str(lastTime) + '\n')
