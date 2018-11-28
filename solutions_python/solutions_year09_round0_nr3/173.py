infile = open('/home/patanjali/Desktop/C-large.in')
outfile = open('/home/patanjali/codejam/C-large.out', 'w')

num_inputs = int(infile.readline().strip())

match_string = 'welcome to code jam'
match_string_len = len(match_string)

for case_no in xrange(num_inputs):
  match_count = [0 for i in xrange(match_string_len)]
  test_string = infile.readline().strip()
  for i in xrange(len(test_string)):
    for j in xrange(0, match_string_len):
      if j == 0 :
	if test_string[i] == match_string[0]:
	  match_count[0] += 1
      else:
	if test_string[i] == match_string[j]:
	  match_count[j] += match_count[j-1]
  outfile.write('Case #%d: %.4d\n' %(case_no+1, match_count[-1]%10000))