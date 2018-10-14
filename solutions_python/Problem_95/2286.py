import sys

translation = {}

def remove_spaces(text):
	return text.replace(" ", "")

def learn_googlerese(original, translated):
	original = remove_spaces(original)
	translated = remove_spaces(translated)
	for i in range(len(translated)):
		letter = translated[i]
		if not translation.has_key(original[i]):
			translation[original[i]] = letter

def translate(text, dic):
	words = text.split(" ")
	translated_words = []
	for word in words:
		translated_word = ""
		for letter in word:
			translated_word += dic[letter]
		translated_words.append(translated_word)
	return " ".join(translated_words)


learn_googlerese("a zoo", "y qee")
learn_googlerese("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi")
learn_googlerese("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
learn_googlerese("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
translation['q'] = 'z'

inverted_translation = dict([v,k] for k,v in translation.items())

#for key, value in translation.items():
#	print key, "->", value

#print translate("a zoo", translation)
#print translate("our language is impossible to understand", translation)
#print translate("enqueue and dequeue", translation)
#print translate("y qee", inverted_translation)

f = open(sys.argv[1])
if f != None:
	T = int(f.readline())
	for t in range(1, T+1):
		G = f.readline().strip()
		print "Case #%d:" % t, translate(G, inverted_translation)

