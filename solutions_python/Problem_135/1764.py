import sys

def solve(infile, outfile):
  num_tests = int(infile.readline().strip())
  for test_num in range(num_tests): 
    first_num = int(infile.readline().strip())
    for row in range(4):
      if row+1 == first_num:
        row_data1 = infile.readline().strip().split(" ")
      else: 
        infile.readline()
    second_num = int(infile.readline().strip())
    for row in range(4):
      if row+1 == second_num:
        row_data2 = infile.readline().strip().split(" ")
      else: 
        infile.readline()
    found = False
    out_str = None
    for x in row_data1: 
      if x in row_data2: 
        if found: 
          out_str = "Bad magician!"
          break
        found = True
        out_str = x
    if out_str: 
      outfile.write("Case #%d: %s\n" % (test_num+1, out_str))
    else:
      outfile.write("Case #%d: Volunteer cheated!\n" % (test_num+1))

if __name__ == "__main__": 
  with open(sys.argv[1], "r") as infile: 
    with open(sys.argv[1] + ".out", "w") as outfile:
      solve(infile, outfile)
  print("Done!")
