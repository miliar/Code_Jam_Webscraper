#!/usr/bin/python2.6

class DancingGooglers(object):
	def __init__(self,input_file,output_file):
		self.input_file=input_file
		self.output_file=output_file
		
	def max_number(self):
		output_file_text = ""
		ifile = open(self.input_file,'r')
		input_file_text_list = ifile.readlines()
		ifile.close()
		
		for i in range(1,int(input_file_text_list[0])+1):
			dancers = map(int,input_file_text_list[i].split(" "))
			num_of_dancers = dancers[0]
			surprise = dancers[1]
			p = dancers[2]
			scores_of_dancer = dancers[3:]
			count = 0
			for score in scores_of_dancer:
				if p*3 <= score or p*3-1 == score or p*3-2 == score:
					count+=1
				elif abs(p*3-4)>score:
					pass
				elif p*3-3 == score or p*3-4 == score:
					if surprise > 0:
						count+=1
						surprise -=1
			output_file_text += "Case #%s: %s\n" % (i,count)
		ofile = open(self.output_file,'w')
		ofile.write(output_file_text)
		ofile.close()
		
		
if __name__ == "__main__":
	input_file = "/home/yogesh/Documents/codejam/B-large.in"
	output_file = "/home/yogesh/Documents/codejam/B-large.out"
	st = DancingGooglers(input_file,output_file)
	st.max_number()

