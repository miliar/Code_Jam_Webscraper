mapping = {
	'z' : 'q',
	'q' : 'z'
}


str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
str1_m = "our language is impossible to understand"
str2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
str2_m = "there are twenty six factorial possibilities"
str3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
str3_m = "so it is okay if you want to just give up"

def solvemapping(str, str_m, mapping):
	words = str.split(" ")
	words_m = str_m.split(" ")
	i = 0
	for word in words:
		j = 0
		for char in word:
			if char not in mapping:
				mapping[char] = words_m[i][j]
			elif mapping[char] != words_m[i][j]:
				print "Different mapping detected: %s should map to %s but maps to %s" % (char, mapping[char], words_m[i][j])
			j += 1
		i += 1	
	return mapping
	
def solvestring(str, mapping, case):
	words = str.split(" ")
	result_string = ""
	for word in words:
		translated_word = ""
		for char in word:
			if char in mapping:
				translated_word += mapping[char]
			else:
				translated_word += "?"
				print "Letter %s has no correct mapping, check it!" % char
		result_string += "%s " % translated_word
	return result_string
	

mapping = solvemapping(str1, str1_m, mapping)
mapping = solvemapping(str2, str2_m, mapping)
mapping = solvemapping(str3, str3_m, mapping)
print "We have %i elements in there." % len(mapping)

input = open("A-small-attempt1.in", "r")
output_file = open("A-small-attempt1.out", "w")
i = 0
solution = ""
for line in input:
	if i == 0:
		i += 1
		continue
	line = line.strip()
	solution = "Case #%i: %s\n" % (i, solvestring(line, mapping, 1))
	output_file.write(solution)
	i += 1
input.close()
output_file.close()