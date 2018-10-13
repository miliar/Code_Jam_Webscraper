import sys, math

#Notes: 
#Practice on small snipet before attempting small or large.
#If they ask for indices, they want indices starting at 1
#Can break out of multiple loops if you match for statement with else continue break
#Main parses file and puts it into a dictionary removing end of line characters
#Function is called from there and rememeber to call output from function

out = open('out.txt', 'w')

def main(filename):
  f = open(filename)
  lst = []
  for line in f:
    lst.append(line.rstrip())
  function(lst)

def function(lst):
  #this can change
  #to split string and cast as ints  use: [int(x) for x in lst[case*3 + 2].split(" ")]
  cases = int(lst[0])
  case = 0
  #this while loop iterates through all caseses. Set desired output for the case 
  #equal to line
  while case < cases:
    #enter solution here
    nums = [int(x) for x in lst[case + 1].split(' ')]
    rad = nums[0]
    paint = nums[1]
    current = 0
    count = -1
    b = 0
    while current <= paint:
      #print paint
      #print current
      count += 1
      current += 2*rad + 1 + b*4
      b += 1
    line = count
    #solution ends here
    case += 1
    output(case, line)

def output(case, sol):
  string = "Case #" + str(case) + ": " + str(sol) + "\n"
  out.write(string)

if __name__ == "__main__":
  arg = sys.argv[1]
  main(str(arg))
  

