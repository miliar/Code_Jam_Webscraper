import math

def main():
	file = open('output', 'w')
	file.close()
	file = open("C-small-attempt7.in")
	with file as f:
		lines = f.readlines()
		loops = int(lines[0]) + 1
		for i in range(1, loops):
			limits = lines[i].split(" ")
			check_fair(i, limits[0], limits[1])
	file.close()

def check_fair(num, inf, sup):
	inf = int(inf)
	sup = int(sup)  + 1
	count = 0

	print "****************************", inf, sup
	for i in range(inf, sup):
		sq = math.sqrt(i)
		if is_int(sq) and is_palindrome(sq) and is_palindrome(i):
			count = count + 1

	file = open('output', 'a')
	file.write("Case #%s: %s\n"%(num, count))
	file.close()

def is_palindrome(s):
	text = "%s"%(int(s))
	new_text = ""
	text_len = len(text) 
	
	for i in range(0, text_len):
		new_text = new_text + text[text_len - 1 - i]

	#print "%s %s %s %s"%(new_text, text, int(new_text), int(text))
	print "%s %s %s"%(s, int(new_text), int(text))
	if(int(new_text) == int(text)):
		print new_text
	return int(new_text) == int(text)

def is_int(s):
	return int(s) == s * 1

main()