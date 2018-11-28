# file1 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/tidy_input.in','r')
# file2 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/tidy_output.txt','w')
file1 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/tidy_input_large.in','r')
file2 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/tidy_output_large.txt','w')

cases = file1.readline()
counter = 0
for line in file1:
	counter += 1
	n = int(line)
	s = str(n)
	if len(s) == 1:
		file2.write("Case #" + str(counter) + ": " + s +"\n")
	else:
		i = len(s) - 1
		while i >= 1:
			if s[i-1] > s[i]:
				s = s[:i-1] + str(int(s[i-1])-1) + "9"*(len(s) - i)
			i -= 1
		file2.write("Case #" + str(counter) + ": " + str(int(s)) +"\n")
file1.close()
file2.close()