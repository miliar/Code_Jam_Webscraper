# file1 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Qualifying Round/Oversized Pancake Flipper/pancake_input.in','r')
# file2 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Qualifying Round/Oversized Pancake Flipper/pancake_output.txt','w')
file1 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Qualifying Round/Oversized Pancake Flipper/pancake_input_large.in','r')
file2 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Qualifying Round/Oversized Pancake Flipper/pancake_output_large.txt','w')


def opposite(s):
	return ''.join("+" if x == "-" else "-" for x in s)

cases = file1.readline()
counter = 0
for line in file1:
	counter += 1
	s, k = line.split()
	k = int(k)
	flips = 0
	for i in range(len(s)-k+1):
		if s[i] == "-":
			s = "".join((s[:i], opposite(s[i:i+k]), s[i+k:]))
			flips += 1
	if "-" in s:
		file2.write("Case #" + str(counter) + ": IMPOSSIBLE\n")
	else:
		file2.write("Case #" + str(counter) + ": " + str(flips) +"\n")
file1.close()
file2.close()

# s = "-+-+-"
# print(s)
# k = 4
# flips = 0
# for i in range(len(s)-k+1):
# 	if s[i] == "-":
# 		s = "".join((s[:i], opposite(s[i:i+k]), s[i+k:]))
# 		print(s)
# 		flips += 1
# if "-" in s:
# 	print("IMPOSSIBLE")
# else:
# 	print(flips)