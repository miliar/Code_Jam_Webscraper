import sys

input = sys.stdin

def solve(mx, shys):
    maxgap = 0
    total = 0
    for j in range(mx+1):
      if maxgap < (j-total):
        maxgap = j-total
      total += int(shys[j])
    return maxgap

for case in range(int(input.readline())):
      values = input.readline().split()
      print("Case #"+ str(case+1) +":", solve(int(values[0]), values[1]))
  
