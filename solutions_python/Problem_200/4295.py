tab = []
n = input()
for testcase in range(int(n)):
		nums = input()
		i = int(nums)
		verif = 0
		result = str(i)
		if i < 10:
			#print('Case #',n,': ',i,'\n')
			tab.append(i)
		else:	
				while True:
					verif2 = 0
					for k in range(len(result)-1):
						if int(result[k])<=int(result[k+1]):
							verif2+=1
					if verif2 != len(result)-1:		
						for j in range(len(result)-1):
							if int(result[j])>int(result[j+1]):
								verif+=1
								new = int(result[j])-1
								string = ""
								for a in range(0,len(result)):
									if a < j:
										string += result[a]
									elif a==j:
										string += str(new)
									if a > j:
										string += '9'
						result = string
					else:
							break                            		
				if verif == 0:
					#print('Case #',n,': ',i,'\n')
					tab.append(i)
				else:
					string = int(string)#print('Case #',n,': ',string,'\n')
					tab.append(string)
for result in range(len(tab)):
		print('Case #'+str((result + 1))+':',tab[result])					