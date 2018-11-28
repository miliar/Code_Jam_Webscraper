import sys

char_dict={' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 'q': 'z', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h', 'z': 'q'}

char_dict1 = {}
for key in char_dict:
  char_dict1[char_dict[key]]=key

def convert_str(s):
  converted_string=""
  for i in s:
    converted_string+=char_dict1[i]
  return converted_string

f= open(sys.argv[1]).read()
f_lines = f.split('\n')
num_times = int(f_lines[0])
for i in range(0, num_times):
  line = f_lines[i+1]
  print "Case #"+str(i+1)+": "+convert_str(line) 

#for line in sys.stdin:
# line_split = line.split(',')
#  count=0 
#  for i in line_split[0]:
#    char_dict[i]=line_split[1][count]
#    count = count + 1

