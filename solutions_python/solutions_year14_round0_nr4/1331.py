
def war(naomi, ken):
	naomi = sorted(naomi)
	ken = sorted(ken)
	vic = 0
	for i in naomi:
		for j in ken:
			if j > i:
				vic += 1
				ken.remove(j)
				break
	return len(naomi) - vic

def deceitful_war(naomi, ken):
	naomi = sorted(naomi, reverse=True)
	ken = sorted(ken, reverse=True)
	vic = 0
	for i in ken:
		b = True
		for j in naomi:
			if j > i:
				b = False
				naomi.remove(j)
				break
		if b:
			naomi = naomi[:len(naomi)-1]
		else:
			vic += 1
	return vic

def main():
	input_file = open('input.txt','r')
	output_file = open('results.txt','w')
	lines = input_file.readlines()
	num_out = int(lines[0])
	for i in xrange(num_out):
		naomi = [float(a.strip()) for a in lines[3*i+2].strip().split(' ')]
		ken = [float(a.strip()) for a in lines[3*i+3].strip().split(' ')]
		output_file.write('Case #'+str(i+1)+': '+ str(deceitful_war(naomi,ken)) + ' ' + str(war(naomi,ken)) +'\n')

if __name__ == '__main__':
	main()