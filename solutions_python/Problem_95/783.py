
def mappingAlpha(filename):
  # opens the input text file in read mode
  f = open(filename)
  # read each line 
  lines = f.readlines()
  first = int(lines[0])
  f = open("output.txt", 'r+')
  for line in range(1,first+1):
    lin = lines[line].rstrip()
    x = "" 
    for word in lin:
      lhs = word
	# the value of action is the value of the getMatch function in the Rule class 
      rhs = Rule.getMatch(lhs)
      x+=rhs
    s = "Case #" + str(line) + ": " + x + "\n"
    f.write(s)	
  f.close()	


# The init function appends the rules in the list.
class Rule:
  rules = []  # a class-level variable: list of the rules
  def __init__(self, leftHandSide, rightHandSide):
    self.lhs = leftHandSide
    self.rhs = rightHandSide
    Rule.rules.append(self)
  def getMatch(value):
    for r in Rule.rules:
      if value == r.lhs:
        return r.rhs
    return False
  getMatch = staticmethod(getMatch)

                          
Rule ("a","y")
Rule ("b","h")
Rule ("c","e")
Rule ("d","s")
Rule ("e","o")
Rule ("f","c")
Rule ("g","v")
Rule ("h","x")
Rule ("i","d")
Rule ("j","u")
Rule ("k","i")
Rule ("l","g")
Rule ("m","l")
Rule ("n","b")
Rule ("o","k")
Rule ("p","r")
Rule ("q","z")
Rule ("r","t")
Rule ("s","n")
Rule ("t","w")
Rule ("u","j")
Rule ("v","p")
Rule ("w","f")
Rule ("x","m")
Rule ("y","a")
Rule ("z","q")
Rule (" "," ")