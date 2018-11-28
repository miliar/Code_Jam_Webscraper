
def get_fitting_groups(g, k):
  sum = 0

  for i in range(len(g)):
    newsum = sum + g[i]
    if newsum > k: 
      p1 = g[:i]
      p2 = g[i:]
      return sum, p2 + p1

    sum = newsum

  return sum, g   

def calculate_earnings(R, k, N, g):
  
  tot = 0

  for i in range(R):
    fg = get_fitting_groups(g, k)
    tot = tot + fg[0]
    g = fg[1]


  return tot    

input = open("C-small-attempt0.in")
output = open("C-small-attempt0.out", "w")

no_of_test_cases = int(input.readline().strip())

for t in range(no_of_test_cases):
  line = input.readline()	
  R, k, N = line.split()
  
  line = input.readline()	
  g = line.split()

  g = [int(i.strip()) for i in g]

  earning = calculate_earnings(int(R.strip()), int(k.strip()), int(N.strip()), g)
  
  out_line = "Case #" + str(t+1) + ": " + str(earning) + "\n"  
  output.write(out_line)
  
input.close()
output.close()
