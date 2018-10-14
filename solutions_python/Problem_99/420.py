out = open('outputA.txt', 'w')
lines = open('inputA.txt', 'r').read().split('\n')

def dPrint(line):
   out.write(line + '\n')
   print line

def mul(a, b):
   return a*b

def keepTyping(a, b):
   allCorrect = reduce(mul, prob[:a])
   #odds of geting it cool at first * 
   sum = (b - a + 1) * allCorrect + (2*b - a + 2) * (1 - allCorrect)
   return sum

def giveUp(a, b):
   sum = b+2
   return sum

def fillBacks(a, b, previousBacks, backs, correctP):
   if previousBacks == a:
      return

   correctP = correctP / prob[a - 1 - previousBacks]
   previousBacks += 1
   backs.append(correctP * (b - a + previousBacks*2 + 1) + (1-correctP)*(b - a + previousBacks*2 + 2 + b))
   fillBacks(a, b, previousBacks, backs, correctP)
   
   
#care with 0 0 0 0
T = int(lines.pop(0))

for t in range(T):
   (A,B) = map(int, lines.pop(0).split(' '))
   prob = map(float, lines.pop(0).split(' '))
   backs = []
   
   fillBacks(A, B, 0, backs, reduce(mul, prob[:A]))
   
   actMin = min(backs)
   actMin = min(actMin, giveUp(A, B))
   actMin = min(actMin, keepTyping(A, B))
   print 'Backs: ', backs
   print 'GiveUp: ', giveUp(A, B)
   print 'Keep: ', keepTyping(A, B)
   
   dPrint('Case #' + str(t+1) + ': ' + str(actMin))