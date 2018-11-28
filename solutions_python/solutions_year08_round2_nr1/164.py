import unittest

def make_trees(n, A, B, C, D, x0, y0, M):
  res = []
  x=x0
  y=y0
  res.append((x, y))
  for i in range(1,n):
    x= (A*x+B)%M
    y=(C*y+D)%M
    res.append((x,y))
  return res

def handle_case(line):
  (n, A, B, C, D, x0, y0, M) = map(int, line.split())
  trees = make_trees(n,A,B,C,D,x0,y0,M)
  # print trees
  res = 0
  for i in range(0, n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        tree1 = trees[i]
        tree2 = trees[j]
        tree3 = trees[k]
        if ((tree1[0]+tree2[0]+tree3[0])%3==0) and ((tree1[1]+tree2[1]+tree3[1])%3==0):
          res=res+1
  return res

def main():
  prefix = "A-small-attempt0"
  input = open(prefix+".in")
  output = open(prefix+".out","w")
  for case in range(1,1+eval(input.readline())):
      res = handle_case(input.readline())
      print "Case #" + str(case) + ": " + str(res)
      output.write("Case #" + str(case) + ": " + str(res)+"\n")
  output.close()
  
if __name__ == "__main__":
  main()
  
class TestCases(unittest.TestCase):
  def test1(self):
    res = handle_case("4 10 7 1 2 0 1 20")
    self.assertEquals(1, res)
  
  def test2(self):
    res = handle_case("6 2 0 2 1 1 2 11")
    self.assertEquals(2, res)
    
  def test3(self):
    res = handle_case("100 2 0 2 1 1 2 11")
    self.assertEquals(2, res)