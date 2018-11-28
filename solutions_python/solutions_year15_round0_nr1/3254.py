import sys
########################################
########################################

def task1_solver(S, audience):

  j = 0
  friends = 0
  sum = 0
  for c in audience:
    cn = int(c)

    #if (i==0) and (cn==0):
    #  friends += 1
    #  continue
    print "j={},cn={},sum={},friends={}".format(j,cn,sum,friends)

    if (cn > 0) and (sum+friends < j):
      friends += j - (sum + friends)

    print "j=", j, ",friends=", friends

    sum += cn
    j += 1
      
    

  #print 'friends=', friends
  return friends



# Solve problem 1
def task1(inputf, outputf):

  # Reading input
  inf = open(inputf, 'r')

  # Writing output
  outf = open(outputf, 'w')

  # Number of test cases
  line = inf.readline()

  n = int(line)
  print 'Number of test cases n = ', n


  for i in range(1,n+1):

    print 'i=', i

    # Read test case
    line = inf.readline()
    splits = line.split()

    S = int(splits[0])
    ss = splits[1]
    print 'S={}, ss={}'.format(S,ss)

    result = task1_solver(S, ss)

    result_str = "Case #{}: {}\n".format(i, result)
    outf.write(result_str)
    print result_str


  # Closing files
  inf.close()
  outf.close()


########################################
########################################
if __name__ == '__main__' : 

  print len(sys.argv)
  print str(sys.argv)

  if len(sys.argv) < 3:
    print "Provide input file and output file"
    sys.exit()

  inputf = sys.argv[1]
  outputf = sys.argv[2]

  print "inputf={}, outputf={}".format(inputf, outputf)

  print "Solving problem ...."
  task1(inputf, outputf)
  
  
