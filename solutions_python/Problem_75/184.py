
data = open("B-large.in", "r")
myout = open("magick_out.txt", "w")
cases = int( data.readline() )

def print_list(list):
  rval = ""
  rval += "["
  for ele in list[:-1]:
    rval += ele + ", "
  if len(list) > 0:
    rval += list[-1]
  rval += "]"
  return rval
  
class Magick:
  def __init__(self):
    self.combine = {}
    self.opposed = {} 
    self.invokes = []
    self.invokes_present = {}
    for ele_i in range(ord('A'),ord('Z')+1):
      self.opposed[ chr(ele_i) ] = []
      self.combine[ chr(ele_i) ] = []
      self.invokes_present[ chr(ele_i) ] = 0
      
  def processCombine(self, combine):
    self.combine[ combine[1] ].append( (combine[0], combine[2] ) )
    self.combine[ combine[0] ].append( (combine[1], combine[2] ) )
    
  def processOpposed(self, opposed):
    self.opposed[ opposed[0] ].append( opposed[1] )
    self.opposed[ opposed[1] ].append( opposed[0] )

  def invoke( self, element ):
    self.add_invoke( element )
    while True:
      changed = self.do_magic()
      if not changed:
        break
    self.try_clear( self.invokes[-1] )
    
  def try_clear(self, element):
    for oppele in self.opposed[ element ]:
      if self.invokes_present[oppele] > 0:
        self.invokes = []
        self.invokes_present = {}
        for ele_i in range(ord('A'),ord('Z')+1):
          self.invokes_present[ chr(ele_i) ] = 0
        return

  def add_invoke(self, element):
    self.invokes.append( element )
    self.invokes_present[element] += 1

  def pop_invoke(self):
    ele = self.invokes[-1]
    self.invokes_present[ ele ] -= 1
    self.invokes.pop()
    
  def do_magic(self):
    changed = False
    if len(self.invokes) < 2:
      return False
    for comb in self.combine[ self.invokes[-1] ]:
      if comb[0] == self.invokes[-2]:
        self.pop_invoke()
        self.pop_invoke()
        self.add_invoke( comb[1] )
        changed = True
        break
    return changed
  

for i in range(0, cases):
  magick = Magick()
  case_data = data.readline().split()
  case_position = 0
  
  combine_count = int(case_data[case_position])
  case_position += 1
  for j in range(0, combine_count):
    magick.processCombine( case_data[case_position] )
    case_position += 1

  opposed_count = int(case_data[case_position])
  case_position += 1
  for j in range(0, opposed_count):
    magick.processOpposed( case_data[case_position] )
    case_position += 1
  
  invokes_count = int(case_data[case_position])
  invokes = case_data[case_position+1]
  
  for j in range(0, invokes_count):
    magick.invoke( invokes[j] )

  myout.write("Case #" + str(i+1) + ": " + print_list(magick.invokes) + '\n')
