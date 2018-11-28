

import sys
import string
import re




def make_translation_table(tranlation_table):
  
  mappings = {};
  mappings[ "ejp mysljylc kd kxveddknmc re jsicpdrysi"]  = "our language is impossible to understand" 
  mappings[ "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"] = "there are twenty six factorial possibilities" 
  mappings[ "de kr kd eoya kw aej tysr re ujdr lkgc jv"] = "so it is okay if you want to just give up" 
  
  
  tranlation_table['y'] = 'a';
  tranlation_table['e'] = 'o';
  tranlation_table['q'] = 'z';
  tranlation_table['z'] = 'q';
  
  for (key, val) in zip( mappings.keys(), mappings.values()):
    for ( ch_f , ch_t ) in zip(key ,val):
      if tranlation_table.has_key( ch_f ):
        if tranlation_table[ch_f] is not ch_t:
          print "error ", ch_f ," old:", tranlation_table[ch_f] , "new:" ,ch_t   
      tranlation_table[ch_f] = ch_t;
  
  
def translate( from_st , tranlation_table ):
    
  to_str = "";
  
  for from_ch in from_st:
    to_str = to_str + tranlation_table[from_ch]
  return to_str;




def solve_problem(input_file_path , output_file_path):
	
	tranlation_table = {} ;
	
	make_translation_table(tranlation_table);
	
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	test_count  = int(input_file.readline());
	
	for index in xrange(test_count):
		translated_string = translate( input_file.readline().strip() , tranlation_table);
		solution_string = "Case #%d: %s"%(index+1,translated_string);			
		print solution_string;
		output_file.write(solution_string+'\n');

	
	input_file.close()
	output_file.close()

	
def  start_me_up():
	if len(sys.argv) == 1:
		print "Usage:"
		print "%s input_file_path [output_file_path]" % ( sys.argv[0]);		
		print "Note: Solution is output to console too." ;		

	elif len(sys.argv) == 2:
		solve_problem(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_problem(sys.argv[1], sys.argv[2]);
		


if __name__ == "__main__":
	start_me_up();


