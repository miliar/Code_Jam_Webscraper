import sys

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
  
  #handle case 1 seperately
  n = 0
  m = 0
  current = 0

  while case < cases:
    #enter solution here
    params = lst.pop(1).rsplit(' ')
    n = int(params[0])
    m = int(params[1])
    i = 1
    rows = []
    line = 'YES'
    while i <= n:
      rows.append([int(val) for val in lst.pop(1).rsplit(' ')])
      i += 1
    for row in rows:
      MAX = max(row)
      for a in range(0, len(row)):
        val = row[a]
        if val < MAX:
          result = column(rows, a, val)
          if result == 'NO':
            line = 'NO'
          
  
  #solution ends here
    case += 1
    output(case, line)


def column(matrix, index, val):
  column = [x[index] for x in matrix]
  for value in column:
    if value > val:
      return 'NO' 
  return 'YES'

def output(case, sol):
  string = "Case #" + str(case) + ": " + str(sol) + "\n"
  out.write(string)

if __name__ == "__main__":
  arg = sys.argv[1]
  main(str(arg))
  

