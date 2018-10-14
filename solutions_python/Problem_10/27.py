import unittest

def handle_case(line1, line2):
  (P,K,L)=map(int, line1.split())
  frequencies=map(int,line2.split())
  frequencies.sort(reverse=True)
  res = 0
  k = 0
  for i in range(1,P+1):
    for j in range(0,K):
      res+=frequencies[k]*i
      k = k+1
      if k >= len(frequencies):
        return res
      
  return res
  

def main():
  prefix = "A-large"
  input = open(prefix+".in")
  output = open(prefix+".out","w")
  line = input.readline().strip()
  for case in range(1,1+int(line)):
      res = handle_case(input.readline().strip(),input.readline().strip())
      print "Case #" + str(case) + ": " + str(res)
      output.write("Case #" + str(case) + ": " + str(res)+"\n")
  output.close()
  
if __name__ == "__main__":
  main()
  
class TestCases(unittest.TestCase):  
  def test1(self):
    res = handle_case("3 9 26", "1 1 1 100 100 1 1 1 1 1 1 1 1 1 1 1 1 10 11 11 11 11 1 1 1 100")
    self.assertEquals(397, res)
