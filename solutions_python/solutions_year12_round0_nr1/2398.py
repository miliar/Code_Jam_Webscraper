def main():
	func=['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
	file_in=open("input.in",'r')
	file_out=open("output.txt",'w')
	cases=int(file_in.readline())
	
	for i in range(cases):
		test=file_in.readline().strip('\n')
		testf=translate(test)
		final=""
		final='Case #'+str((i+1))+': '+str(testf)+'\n'
		#print final
		file_out.write(final)

def translate(test):
	func=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
	testf=""
	for i in test:
		if str(i)==' ':
			testf=str(testf)+' '
		else:
			index=(ord(i))-97
			testf=str(testf)+str(func[index])
			
	return testf

main()
		
	
