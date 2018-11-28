import sys

def get_mappings():
	mappings_dict = {
		'a': 'y',
		'o': 'k',
		'z': 'q',
		'q': 'z',
	}

	input_list = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 
		      'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
		      'de kr kd eoya kw aej tysr re ujdr lkgc jv',]

	output_list = ['our language is impossible to understand',
		       'there are twenty six factorial possibilities',
		       'so it is okay if you want to just give up',]

	for in_str, out_str in zip(input_list, output_list):
		#turn output into list
		o_list = list(out_str)
		for index, letter in enumerate(in_str):
			
			translation = o_list[index]
			if letter not in mappings_dict:
				mappings_dict[letter] = translation 
	#import pdb; pdb.set_trace()
	return mappings_dict
			
		



if __name__ == '__main__':
	mappings_dict = get_mappings()
	f = open(sys.argv[1])
	total = f.readline().strip()
	i = 1
	for line in f:
		line = line.strip()
		if not line:
			continue
		translated = [mappings_dict[x] for x in line]
		print 'Case #%d: %s' % (i, ''.join(translated))
		i += 1
