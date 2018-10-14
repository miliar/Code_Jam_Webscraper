pin = []

def getPin(x):
	return pin[x-1]	


x = raw_input().split()

for i in range(0,len(x)):
	x[i] = int(x[i])

m = x[0]

n = x[1]

for i in range(0,m):
	x = input()
	pin.append(x)

city  = {}

for i in range(1,m+1):
	city[i] = []

for i in range(0,n):
	x = raw_input().split()
	for i in range(0,len(x)):
		x[i] = int(x[i])
	temp = []
	temp.append(x[1])
	if x[0] not in city:
		city[x[0]] = [x[1]]
		city[x[1]] = [x[0]]
	else:
		city[x[0]]+= [x[1]]
		city[x[1]]+= [x[0]]

print city
cur = pin.index(min(pin)) + 1
nonVisit = []
for i in city:
	nonVisit.append(i)
visited = []
temp = []
temp1 = []
final=[]
final.append(getPin(cur))
visited.append(cur)
print visited
temp+=city[cur]
print temp
for i in temp:
	temp1.append(getPin(i))
print temp1



while(len(temp)!=0):
	
	minpin = min(temp1)
	final.append(minpin)
	minc = pin.index(minpin) + 1
	print minpin,minc
	visited.append(minc)
	temp.pop(temp.index(minc))
	temp1.pop(temp1.index(minpin))
	for i in city[minc]:
		if i not in visited:
			temp.append(i)
			temp1.append(getPin(i))

print final 	
	

