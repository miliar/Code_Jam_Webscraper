#! /usr/bin/python

__author__ = "assim"
__date__ = "$May 22, 2010 7:28:41 AM$"

def solve(exist_d, tobemade_l):
	mkdir_count = 0
	for p in tobemade_l:
		exist_count = is_exist(exist_d, p)
		if not exist_count:
			continue
		mkdir_count += exist_count
		exist_d = add_path(exist_d, p)
	return mkdir_count

def is_exist(d,path_list):
	retValue = 0
	for p in path_list:
		if not retValue:
			if p not in d:
				retValue += 1
			else:
				d = d[p]
		else:
			retValue += 1
	return retValue
def merge_dictionary(dst, src):
    stack = [(dst, src)]
    while stack:
        current_dst, current_src = stack.pop()
        for key in current_src:
            if key not in current_dst:
                current_dst[key] = current_src[key]
            else:
                if isinstance(current_src[key], dict) and isinstance(current_dst[key], dict) :
                    stack.append((current_dst[key], current_src[key]))
                else:
                    current_dst[key] = current_src[key]
    return dst

def add_path(d, path_list):
	global root_dir
	temp = {}
	path_list.reverse()
	for p in path_list:
		temp = {p:temp}
	d = merge_dictionary(d, temp)
	return d

def parse(p="a-l"):
	#	R...
	#	BR..
	#	BR..
	#	BR..
	input = open("io/%s-i" % (p), "r")
	output = open("io/%s-o" % (p), "w")
	output_str_list = []
	num_cases = int(input.readline())
	for case in xrange(num_cases):
		_exist, _tobemade = input.readline().split()
		exist, tobemade = int(_exist), int(_tobemade)
		exist_d = {}#defaultdict(dict)
		for row in xrange(exist):
			# @type input file
			_path = input.readline().strip().split("/")[1:]
			exist_d = add_path(exist_d, _path)
		#print exist_d
		tobemade_l = []#defaultdict(dict)
		for row in xrange(tobemade):
			_path = input.readline().strip().split("/")[1:]
			tobemade_l.append(_path)
		output_str_list.append("Case #%s: %s" % (case + 1, solve(exist_d, tobemade_l)))
		#output.write("Case #%s: %s" % (case + 1, solve(int(n), int(k))))
		#output.write("\n")
	input.close()
	output.write("\n".join(output_str_list))
	output.close()







if __name__ == "__main__":
	parse()
