import sys
sys.path.append('users/ahn/desktop/codejam/round 1A')

file = open('input.txt')
input = file.read()
file.close()

T = int(input.split('\n')[0])

N = []
PD = []
PG = []

for i in range(0,T):
	temp = input.split('\n')[i+1].split(' ')
	N += [int(temp[0])]
	PD += [int(temp[1])]
	PG += [int(temp[2])]
	
def gcd(a,b):
	if a == 0:
		return b
	elif b == 0:
		return a
	elif a == b:
		return a
	else:
		if a>b:
			if a%b == 0:
				return b
			else:
				return gcd(b,a%b)
		else:
			if b%a == 0:
				return a
			else:
				return gcd(a,b%a)

possibility = []

for i in range(0,T):
	possibility += [True]

for i in range(0,T):
	if PG[i] == 0 and PD[i] == 0:
		possibility[i] = True
	elif PG[i] == 0 and PD[i] > 0:
		possibility[i] = False
	elif PG[i] == 100 and PD[i] < 100:
		possibility[i] = False
	else:
		today_min = 100/gcd(100,PD[i])
		if today_min > N[i]:
			possibility[i] = False

output = ''

for i in range(0,T):
	output += 'Case #'+str(i+1)+': '
	if possibility[i]:
		output += 'Possible\n'
	else:
		output += 'Broken\n'
		
file = open('output.txt','w')
file.write(output)
file.close()