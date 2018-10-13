def main():
	testcases = input()

	for test in range(0,testcases):
		detail = raw_input()
		details = detail.split()
		counter =0
		A= int(details[0])
		B= int(details[1])
		K= int(details[2])

		for i in range (0,A):
			for j in range(0,B):
				if (i & j)< K:
					counter +=1
		cases=test+1
		print 'Case #'+ str(cases) + ': ' + str(counter )
		
		test +=1	

if __name__ == "__main__":
	main()
