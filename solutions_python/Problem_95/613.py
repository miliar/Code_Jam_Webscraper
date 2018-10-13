# -*- coding: utf-8 -*-

import sys

class Googlerese:
	def learn(self,training_data_set):
		self.convert_dict={}
		for training_data in training_data_set:
			src_sentence,dst_sentence = training_data
			
			for idx in range(len(src_sentence)):
				self.convert_dict[src_sentence[idx]] = dst_sentence[idx]

		alphabets=set(list("abcdefghijklmnopqrstuvwxyz"))
		
		key_set=set(self.convert_dict.keys())
		val_set=set(self.convert_dict.values())
		
		rest_key_set = alphabets - key_set
		rest_val_set = alphabets - val_set
		
		#print "rest_key_set:%s,rest_val_set:%s"%(rest_key_set,rest_val_set)
		
		if len(rest_key_set) == 1 and len(rest_val_set) == 1:
			self.convert_dict[rest_key_set.pop()]=rest_val_set.pop()
			
		
	def show_dict(self):
		for k in sorted(self.convert_dict.keys()):
			print "%s\t%s"%(k,self.convert_dict[k])

	def translate(self,src_sentence):
		dst_sentence = ""
		for idx in range(len(src_sentence)):
			dst_sentence += self.convert_dict[src_sentence[idx]]
		return dst_sentence

googlerese=Googlerese()

training_data_set = [
					["y qee","a zoo"],
					["ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"],
					["rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"],
					["de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up"],
				]

googlerese.learn(training_data_set)
#googlerese.show_dict()

f=open(sys.argv[1])
f2=open(sys.argv[2],'w')

lines=f.read().split('\n')

for idx in range(int(lines[0])):
	english_sentence = googlerese.translate(lines[idx+1])
	f2.write("Case #%d: %s\n"%(idx+1,english_sentence))
f2.close
