import pdb

#input_filename = 'A-small-attempt0.in'
input_filename = 'A-large.in'
input_file = open(input_filename)
output_file = open(''.join(('output_',input_filename)), 'w')
num_cases = int(input_file.readline())

for case_number in xrange(num_cases):
  line  = input_file.readline()
  snappers, snaps = map(int, line.split())
  if ((snaps - (2**snappers-1)) % (2**snappers)) is 0:
    state = 'ON'
  else:
    state = 'OFF'
  string = 'Case #' + str(case_number+1) + ': ' + str(state) + '\n'
  output_file.write(string)

output_file.close()
input_file.close()
