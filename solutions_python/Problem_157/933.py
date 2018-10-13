#INPUT = 'dijkstraTest.txt'
#OUTPUT = 'dijkstraTestOutput.txt'
INPUT = 'C-small-attempt3.in'
OUTPUT = 'CSmallOutput3.txt'
#M = [['-1', 'k', '-j']['j', '-k', '-1']['k', 'j', '-i']]
d = {'i':{'i':'-1', 'j':'k', 'k':'-j', '1':'i'},
     'j':{'i':'-k', 'j':'-1', 'k':'i', '1':'j'}, 
     'k':{'i':'j', 'j':'-i', 'k':'-1', '1':'k'},
     '1':{'i':'i', 'j':'j', 'k':'k', '1':'1'}}

class Item:
   def __init__(self, letter, negative):
      self.l = letter
      self.n = negative
      
   def multiply(self, i):
      l2 = d[self.l][i.l]
      n2 = False
      if len(l2)==2:
         n2 = True
         l2 = l2[1]
      n2 = (self.n != n2)!=i.n 
      return Item(l2, n2)
   
   def __eq__(self, i):
      return self.l==i.l and self.n == i.n
   
   def __str__(self):
      if self.n:
         return '-'+ self.l
      return self.l

def getI(length, stng):
   current = Item('1', False)
   for n in range(length):
      current = current.multiply(Item(stng[n], False))
      if current == Item('i', False):
         return n
   return None

         
def getK(length, stng):
   current = Item('1', False)
   for n in range(length-1, -1, -1):
      current = Item(stng[n], False).multiply(current)
      if current == Item('k', False):
         return n
   return None       
   
def getJ(stng, start, end):
   current = Item('1', False)
   for n in range(start+1, end):
      current = current.multiply(Item(stng[n], False))
   if current == Item('j', False):
      return n
   return None
      
      
def solve(length, stng):
   i = getI(length, stng)
   if i==None: # will this work?
      return False
   k = getK(length, stng)
   if k==None:
      return False
   if k<=i:
      print('crossed')
      return False
   j = getJ(stng, i, k)
   if j==None:
      return False
   return True
    
               
def getInput(filename):
   file = open(filename, 'r')
   stng = file.read().split()
   file.close()
   return stng

def YesOrNo(b):
   if b:
      return 'YES'
   return 'NO'
#def simplify(stng):
   #for n in stng:
      
def main():
   stng = getInput(INPUT)
   trials = int(stng[0])
   stng = stng[1:]
   f = open(OUTPUT, 'w')
 
   for n in range(trials):
      L = int(stng[n*3])
      X = int(stng[n*3+1])
      s = stng[n*3+2]
      f.write('Case #'+str(n+1)+': ' + YesOrNo(solve(L*X, s*X)))
      if not n == trials-1:
         f.write('\n')
main()
       
