import sys

def process_case(lines):
  first_guess = int(lines[0])
  second_guess = int(lines[5])
  first_nums = [int(x) for x in lines[first_guess].split()] 
  second_nums = [int(x) for x in lines[second_guess+5].split()]
  num_matches = 0
  first_match = 0
  print first_nums, second_nums
  for x in range(0, 4):
    for y in range(0, 4):
      if first_nums[x] == second_nums[y]:
        print 'match found for ', first_nums[x] , ' =', second_nums[y]
        num_matches+=1
        first_match = first_nums[x]

  if num_matches == 0:
    return 'Volunteer cheated!'
  elif num_matches == 1:
    return str(first_match)
  elif num_matches >1:
    return 'Bad magician!'
  

def main():
  
  testcases=0
  lines = []
  output = []
  with open(sys.argv[1]) as file:
    testcases = int(file.readline())
    for x in range(0, testcases):
      print "case#" + str(x+1)
      for i in range(0, 10):
        lines.append(file.readline())
      output.append(process_case(lines))
      lines = []


  for x in range(0, len(output)):
    print 'Case #'+str(x+1)+':', output[x]
        


if __name__ == '__main__':
  main()
