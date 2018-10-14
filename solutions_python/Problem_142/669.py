#import pdb; pdb.set_trace()

def main():
  testcases = int(input())
  for caseNr in range(1, testcases+1):
    n = int(input().strip())
    ss = [0 for i in range(n)]
    for i in range(n):
      ss[i] = input().strip()

    sol = solve(ss)
    if sol > -1:
      print("Case #%i: %i" % (caseNr, sol))
    else:
      print("Case #%i: Fegla Won" % caseNr)

def solve(ss):
  l0 = len(ss[0])
  l1 = len(ss[1])
  if ( l0 > l1 ):
    s0 = ss[0]
    s1 = ss[1]
  else:
    s0 = ss[1]
    s1 = ss[0]
  xl = max(l0,l1)
  nl = min(l0,l1)
  d = [[-1 for i in range(nl+1)] for j in range(xl+1)]
  d[0][0] = 0
  # print(s0,s1)
  # print(d)
  # print(xl,nl)
  for i in range(1,xl+1):
    for j in range(1,nl+1):
      if d[i-1][j-1] > -1 and s0[i-1] == s1[j-1]:
        d[i][j] = d[i-1][j-1]
      elif d[i][j-1] > -1 and s1[j-1] == s1[j-2]:
        d[i][j] = d[i][j-1]+1
      elif d[i-1][j] > -1 and s0[i-1] == s0[i-2]:
        d[i][j] = d[i-1][j]+1
      # print(i,j,d[i][j])
  # print(d)
  return d[xl][nl]

if __name__ == "__main__":
  main()

'''
' Integers
'''
# Read an integer
#n = int(inputFile.readline().strip())

# Read a list of integers
#n_list = map(int, inputFile.readline().strip().split())

# Read a matrix of integers
#n_matrix = []
#for i in range(n):
#    n_matrix.append(map(int, inputFile.readline().strip().split()))

'''
' Floats
'''
# Read a float
#f = float(inputFile.readline().strip())

# Read a list of flots
#f_list = map(float, inputFile.readline().strip().split())

'''
' Strings
'''
# Read a string
# s = inputFile.readline().strip()