import sys

RULES = {"y" : "a", 
		 "e" : "o", 
		 "q" : "z",
		 "z" : "q"}


def learn_from_sample(original, decrypted):
	for i in range(0, len(decrypted)): RULES[original[i]] = decrypted[i]

def decrypt(original):
	return ''.join([RULES[original[i]] for i in range(0, len(original))])
	
def main():
	learn_from_sample("ejp mysljylc kd kxveddknmc re jsicpdrysi",
				  "our language is impossible to understand")

	learn_from_sample("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					  "there are twenty six factorial possibilities")
					  
	learn_from_sample("de kr kd eoya kw aej tysr re ujdr lkgc jv",
					  "so it is okay if you want to just give up")
					  
	text = sys.stdin.readlines()
	for i in range(1, int(text[0]) + 1):
		print "Case #{0}: {1}".format(i, decrypt(text[i][:-1]))
	
if __name__ == "__main__":
    main()
