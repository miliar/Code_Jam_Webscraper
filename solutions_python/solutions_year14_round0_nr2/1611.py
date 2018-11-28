# Cookie Clicker Aplha
#
# by Enrique Gonzalez (Enriikke)
# enjoy!


from decimal import *

############### FILE NAMES ###############
input = 'B-large.in'
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
        c, f, x = map(Decimal, file.readline().split())

        return c, f, x

    except Exception as e:
        print type(e)
        print e.args


def cookies(c, f, x, t, r):
  if t >= x:
    return 0
  elif c >= x:
    return x / r
  elif t >= c:
    s1 = (x - t) / r
    s2 = x / (r + f)

    if s1 <= s2:
      return s1
    else:
      return cookies(c, f, x, 0, r + f)
  else:
    s1 = x / r
    s2 = c / r

    if s1 <= s2:
      return s1
    else:
      return s2 + cookies(c, f, x, c, r)



def cookies_loop(c, f, x, t, r):
  s = Decimal(0)
  if c >= x:
    return x / r

  while t < x:
    if t >= c:
      s1 = (x - t) / r
      s2 = x / (r + f)

      if s1 <= s2:
        s += s1
        t = x
      else:
        t = 0
        r += f
    else:
      s1 = x / r
      s2 = c / r

      if s1 <= s2:
        s += s1
        t = x
      else:
        s += s2
        t += c

  return s




# Solve the problem!!
def solve():
    # Open the files needed.
    input_file, output_file = open_files(input, output)

    # Get the total number of cases.
    total_cases = int(input_file.readline())
    for case in xrange(1, total_cases + 1):

        #Get the case data.
        farm_cost, farm_rate, cookie_goal = parse_data(input_file)
        starting_cookies = Decimal(0)
        starting_rate = Decimal(2)

        # Do all the magic here.
        solution = cookies_loop(farm_cost, farm_rate, cookie_goal, starting_cookies, starting_rate)
        solution = solution.quantize(Decimal('.0000000'))

        # Print solution to file.
        print_solution(case, solution, output_file)


    # Close the files used.
    input_file.close()
    output_file.close()



#import cProfile
#cProfile.run('solve()')
solve()
