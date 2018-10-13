#!/usr/bin/python2.6

class SpeakingTongues(object):
	def __init__(self,input_file,output_file):
		self.input_file=input_file
		self.output_file=output_file
		
	def translation(self):
		replace_word_dic = {
			'a':'y','b':'h','c':'e','d':'s','e':'o',
			'f':'c','g':'v','h':'x','i':'d','j':'u',
			'k':'i','l':'g','m':'l','n':'b','o':'k',
			'p':'r','q':'z','r':'t','s':'n','t':'w',
			'u':'j','v':'p','w':'f','x':'m','y':'a',
			'z':'q',' ':' '
			}
		output_file_text = ""
		ifile = open(self.input_file,'r')
		input_file_text = ifile.read()
		ifile.close()
		
		input_file_text_list = input_file_text.split("\n")
		for i in range(1,int(input_file_text_list[0])+1):
			output_file_text += "Case #%s: %s\n" % (i,"".join(replace_word_dic[letter] for letter in input_file_text_list[i]))
		
		ofile = open(self.output_file,'w')
		ofile.write(output_file_text)
		ofile.close()
		
		
if __name__ == "__main__":
	input_file = "/home/yogesh/Documents/codejam/A-small-attempt0.in"
	output_file = "/home/yogesh/Documents/codejam/A-small-attempt0.out"
	st = SpeakingTongues(input_file,output_file)
	st.translation()

