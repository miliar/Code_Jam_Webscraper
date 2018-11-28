if __name__ == '__main__':
	caseNum = int(input())

	for i in range(caseNum):
		n = input()
		ln = list(n)
		post = 0
		if len(ln) == 1:
			result = n
		else:
			while post < len(ln)-1 and ln[post] <= ln[post+1]:
				post += 1

			if post == len(ln)-1:
				result = ''.join(ln)
			else:
				for j in range(post+1,len(ln)):
					ln[j] = '9'
				while ln[post] == ln[post-1] and post > 0:
					ln[post] = '9'
					post -= 1

				ln[post] = str(int(ln[post])-1)

				if ln[0] == '0':
					result = ''.join(ln[1:]) 
				else:
					result = ''.join(ln)

		print("Case #{}: {}".format(i+1,result))