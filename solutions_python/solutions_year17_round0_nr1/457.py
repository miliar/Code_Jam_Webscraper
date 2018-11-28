readFile = open("A-large.in")
testCases = eval(readFile.readline())
ans = {}
for t in range(0,testCases):
    string,k = map(str, readFile.readline().split())
    i = 0
    flip = 0
    arr = [string[l] for l in range(0,len(string))]
    impossible = False
    while i < len(arr):
	if arr[i] == '-':
	   count = 0
	   j = i
	   if len(arr[i:]) >= int(k):
	   	while count < int(k):
		    if arr[j] == '-':
	           	arr[j] = '+'
		    else:
		        arr[j] = '-'
		    j += 1
		    count += 1
		flip += 1
	   else:
		impossible = True
		break;
	i += 1
    if impossible:
	ans[t] = 'IMPOSSIBLE'
    else:
    	ans[t] = flip

outputFile = open("A-Large-output.txt",'w')
for i in range(0,len(ans)):
    outputFile.write("Case #%d: %s\n" % (i+1,ans[i]))

