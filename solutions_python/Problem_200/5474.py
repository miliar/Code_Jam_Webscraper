import sys

fo = open(sys.argv[1])
fw = open(sys.argv[1]+'.output', 'w')


def is_tidy(num):
	num = long(num)
	digits = []
	while num!=0:
		digits.append(num%10)		
		num = num/10
	for i in range(len(digits)-1):
		if digits[i]<digits[i+1]:
			return False
	return True


i = 0
for line in fo:
	i += 1
	if i==1:
		continue
	num = long(line.strip())
	for j in range(num,0,-1):
		if is_tidy(j):
			fw.write("Case #%d: %d\n" %(i-1,j))
			break

fo.close()
fw.close()