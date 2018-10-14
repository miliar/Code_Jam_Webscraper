#!/usr/bin/python2.6

class RecycledNumbers(object):
	def __init__(self,input_file,output_file):
		self.input_file=input_file
		self.output_file=output_file
		
	def get_count(self):
		output_file_text = ""
		ifile = open(self.input_file,'r')
		input_file_text_list = ifile.readlines()
		ifile.close()
		
		for i in range(1,int(input_file_text_list[0])+1):
			num_range = map(int,input_file_text_list[i].split(" "))
			num_list = []
			for num in range(num_range[0],num_range[1]):
				str_num = str(num)
				for num_i in range(1,len(str_num)):
					recycle_num = str_num[-num_i:] + str_num[:-num_i]
					if num_range[0] <= num < int(recycle_num) <= num_range[1]:
						num_list.append(":%s:%s:" % (num,recycle_num))
			output_file_text += "Case #%s: %s\n" % (i,len(set(num_list)))
		ofile = open(self.output_file,'w')
		ofile.write(output_file_text)
		ofile.close()
		
		
if __name__ == "__main__":
	input_file = "/home/yogesh/Documents/codejam/C-large.in"
	output_file = "/home/yogesh/Documents/codejam/C-large.out"
	st = RecycledNumbers(input_file,output_file)
	st.get_count()

