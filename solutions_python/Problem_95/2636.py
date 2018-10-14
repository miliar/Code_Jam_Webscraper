import os

g_to_e_dictionary = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q' }

def translate_letter(letter):
	return g_to_e_dictionary[letter]

def translate_sentence(sentence):
	letter_list = list(sentence)
	data = []
	for letter in letter_list:
		if letter == ' ':
			data.append(' ')
		else:
			data.append(translate_letter(letter))
	return ''.join(data)

def translate_sentences(sentences):
	translated_sentences = []
	for sentence in sentences:
		translated_sentences.append(translate_sentence(sentence))
	return translated_sentences

def read_file(filename):
	sentences_array = []
	FILE = open(filename, "r")
	number_of_sentences = int(FILE.readline())
	for i in range(0, number_of_sentences):
		sentences_array.append(FILE.readline().strip())
	FILE.close()
	return sentences_array

def write_file(filename, sentences):
	FILE = open(filename, "w")
	for idx, sentence in enumerate(sentences):
		prefix = "Case #" + str(idx+1) + ": "
		FILE.write(prefix + sentence + '\n')
	FILE.close()

if __name__ == "__main__":
	sentences_array = read_file('A-small-attempt1.in')
	translated_sentences_array = translate_sentences(sentences_array)
	write_file('output.txt', translated_sentences_array)
