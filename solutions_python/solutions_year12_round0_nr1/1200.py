prtdir = '/home/rajkumar/google-codejam/Tongue/'
input = open(prtdir+ 'input.txt','r')
inputmap = open(prtdir+ 'mapper.txt','r')
output = open(prtdir+'output.txt','w')

map = {}
lines = []
for i in range(6):
	lines.append(inputmap.readline().rstrip())

for i in range(3):
	cryptost = list(lines[i])
	decryptst = list(lines[i+3])
	for j in range(len(cryptost)):
		map[cryptost[j]] = decryptst[j]

map['q'] = 'z'
map['z'] = 'q'

testcases = int(input.readline())

for i in range(testcases):
	crytostrg = list(input.readline().rstrip())
	decrypto = []
	for kw in crytostrg:
		decrypto.append(map[kw])
	output.write('Case #'+ str(i+1) +': '+''.join(decrypto)+'\r\n')
	


output.close()