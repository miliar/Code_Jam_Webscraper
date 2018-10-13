
def findRowOfInterest(f):
  row = int(f.readline())-1
  row_of_interest = set()
  for i in xrange(0,4):
    current_row = f.readline()
    if i == row:
      row_of_interest = set([int(x) for x in current_row.split(' ')]) 
  return row_of_interest 

def write_to_output_file(case,o,i):
  opt = len(i)
  if(opt == 1):
    o.write('Case #%i: %i\n'%(case,i.pop()))
  elif(opt == 0):
    o.write('Case #%i: Volunteer cheated!\n'%(case))
  else:
    o.write('Case #%i: Bad magician!\n'%(case))


with open('sample.txt','rb') as f, open('solution.txt','wb') as o:
  number_of_test_cases = int(f.readline())
  for case in xrange(0,number_of_test_cases):
    first_row_of_interest = findRowOfInterest(f)
    second_row_of_interest = findRowOfInterest(f)
    write_to_output_file(case+1,o,first_row_of_interest.intersection(second_row_of_interest))

