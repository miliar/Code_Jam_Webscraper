phrase="welcome to code jam"

def rec(manque,reste):
	if len(manque)==0:
		return 1
	if reste.count(manque[0])==0:
		return 0
	i=0
	while(reste.count(manque[0])>0):
		i+= rec(manque[1:],reste[reste.index(manque[0])+1:])
		reste=reste[reste.index(manque[0])+1:]
	return i
		
		
def main():
	f = open('input.in','r')
	fout = open('output.out','w')

	
	case = 1
	for text in f.readlines()[1:]:
		text=text.strip("\n")
		print text
		
		
		
		
		
		
		output = "Case #%i: " % case
		output += str(10000 + rec(phrase,text))[-4:]
		output += '\n'
		case+=1
		
		fout.writelines(output)
		print output
		
	fout.close()
	
if __name__ == '__main__':
	main()