# Deceitful War
#
# by Enrique Gonzalez (Enriikke)
# enjoy!



############### FILE NAMES ###############
input = 'D-large.in'
output = 'data.out'



# Open (create) the files needed to read the data and write the solution.
def open_files(input, output):
  try:
    input_file = open(input, 'r')
    output_file = open(output, 'w')

    return input_file, output_file

  except Exception as e:
    print type(e)
    print e.args



# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file):
  try:
    file.write('Case #{0!s}: {1}\n'.format(case_number, solution))

  except Exception as e:
    print type(e)
    print e.args



# Read the data for a single case from the input file.
def parse_data(file):
  try:
    b = int(file.readline())
    n = sorted(map(float, file.readline().split()), reverse=True)
    k = sorted(map(float, file.readline().split()), reverse=True)

    return b, n, k

  except Exception as e:
    print type(e)
    print e.args



# Solve the problem!!
def solve():
  # Open the files needed.
  input_file, output_file = open_files(input, output)

  # Get the total number of cases.
  total_cases = int(input_file.readline())
  for case in xrange(1, total_cases + 1):

    #Get the case data.
    blocks, naomi, ken = parse_data(input_file)
    naomi_fair = list(naomi)
    ken_fair = list(ken)

    # Do all the magic here.
    solution = [0, blocks]
    while len(naomi) > 0:
      n = naomi_fair.pop(-1)
      l = len(ken_fair)
      for i in xrange(l):
        if ken_fair[l - 1 - i] > n:
          ken_fair.pop(l - 1 - i)
          solution[1] -= 1
          break

      if naomi[0] > ken[0]:
        naomi.pop(0)
        ken.pop(0)
        solution[0] += 1
      else:
        naomi.pop(-1)
        ken.pop(0)



    solution = '{0!s} {1!s}'.format(solution[0], solution[1])

    # Print solution to file.
    print_solution(case, solution, output_file)


  # Close the files used.
  input_file.close()
  output_file.close()



#import cProfile
#cProfile.run('solve()')
solve()
