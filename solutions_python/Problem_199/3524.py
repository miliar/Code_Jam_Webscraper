n = int(input())
for i in list(range(n)):
	#print(i)
	s = input().strip().split()
	k = s[1]
	s = list(s[0])
	#s = str(s)
	k = int(k)
	#print(s, k)
	count = 0
	for j in range(len(s) - k + 1):
	  if s[j] == '-':
	    count += 1
	    for l in range(k):
	      #print(l)
	      if s[j + l] == '-':
	        s[j + l] = '+'
	      else:
	       s[j + l] = '-'
	    #print(s)
	flag = 0
	for j in range(len(s)):
	  if s[j] == '-':
	    print('case #' + str(i + 1) + ': IMPOSSIBLE')
	    flag = 1
	    break
	if flag == 0:
	  print('case #' + str(i + 1) + ': ' + str(count))