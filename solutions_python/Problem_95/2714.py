import sys;
import json;

abet = [i for i in range(0, 26)];

def main():
	cmap = calc_map();
	
	T = input();
	G = list();

	for i in range(0, int(T)):
		G.append(input());

	for i in range(0, int(T)):
		print("Case #%d: %s" % (i+1, translate(G[i], cmap)));

def translate(sentence, cmap):
	def f(letter):
		return cmap[letter];

	english = "".join([f(l) for l in sentence]);

	return english;

def calc_map():
	googlerese = [
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	];
	english = [
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
	];

	test = {};
	for i,sentence in enumerate(english):
		sentence_g = googlerese[i];

		for j,letter in enumerate(sentence):
			letter_g = sentence_g[j];

			test[letter_g] = letter;

	test['q'] = 'z';
	test['z'] = 'q'; 
	return test;
if __name__ == "__main__":
	main();
